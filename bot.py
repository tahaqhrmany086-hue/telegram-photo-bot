from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ======== توکن ربات ========
TOKEN = "8569797827:AAFHYYs_ToF4GWlGCQ0PvJ4BV4794VQGNxk"

# ======== آیدی عددی گروه ========
GROUP_ID = -1003703278551  # همین که دادی

async def forward_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # فقط عکس‌ها رو فوروارد می‌کنه
    await context.bot.forward_message(
        chat_id=GROUP_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id
    )

# ساخت ربات
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, forward_photo))

# ربات شروع می‌کنه به گوش دادن پیام‌ها
app.run_polling()
