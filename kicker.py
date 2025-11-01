from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.error import TelegramError

# Your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

async def handle_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle new members joining the group"""
    
    message = update.message
    chat = message.chat
    
    # Check if there are new members
    if not message.new_chat_members:
        return
    
    # Get the user who added the new members
    added_by = message.from_user
    
    # Check if the person who added is an admin or owner
    try:
        chat_member = await context.bot.get_chat_member(chat.id, added_by.id)
        is_admin = chat_member.status in ['creator', 'administrator']
    except TelegramError:
        is_admin = False
    
    # If added by admin/owner, allow it
    if is_admin:
        return
    
    # Check each new member
    for new_member in message.new_chat_members:
        # Check if the new member is a bot
        if new_member.is_bot:
            # Don't kick ourselves
            bot_info = await context.bot.get_me()
            if new_member.id == bot_info.id:
                continue
            
            try:
                # Kick the bot
                await context.bot.ban_chat_member(chat.id, new_member.id)
                # Unban immediately so it can be added again later by admins
                await context.bot.unban_chat_member(chat.id, new_member.id)
                
                # Send notification message
                await message.reply_text(
                    f"Bot @{new_member.username or new_member.first_name} was removed.\n"
                    f"Only admins can add bots to this group."
                )
            except TelegramError as e:
                print(f"Error kicking bot: {e}")

def main():
    """Start the bot"""
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handler for new members
    application.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_new_members)
    )
    
    # Start the bot
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
