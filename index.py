‎# -----------------------------
‎# Telegram Video Bot (Working)
‎# -----------------------------
‎
‎from telegram import Update
‎from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
‎
‎# ========== SETTINGS ==========
‎BOT_TOKEN = "8416258513:AAFifIR-z97mWvMp9gvdZqe14PFKDUjn_6s"        # Apna bot token yahan daalein
‎CHANNEL_USERNAME = "shapatergroup"  # Apna channel username
‎OWNER_ID = "7797456931"                      # Apna Telegram ID
‎
‎# In-memory video list (temporary, restart ke baad reset hoti hai)
‎VIDEOS = []
‎
‎# ===============================
‎# START COMMAND
‎# ===============================
‎async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
‎    user = update.effective_user
‎
‎    # Channel join check
‎    try:
‎        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user.id)
‎        if member.status in ["member", "administrator", "creator"]:
‎            # User joined channel, videos show karo
‎            if VIDEOS:
‎                video_list = "\n".join(VIDEOS)
‎                await update.message.reply_text(f"✅ Aap channel join kar chuke ho.\n\n📹 Available Videos:\n{video_list}")
‎            else:
‎                await update.message.reply_text("✅ Aap channel join kar chuke ho.\n\n📹 Abhi koi video upload nahi hui.")
‎        else:
‎            raise Exception("Not joined")
‎    except:
‎        await update.message.reply_text(
‎            f"❌ Pehle {CHANNEL_USERNAME} channel join karein.\n\nPhir /start likhein."
‎        )
‎
‎# ===============================
‎# UPLOAD VIDEO (ONLY OWNER)
‎# ===============================
‎async def upload_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
‎    user = update.effective_user
‎    text = update.message.text.strip()
‎
‎    # Sirf owner allowed
‎    if user.id != OWNER_ID:
‎        await update.message.reply_text("❌ Sirf owner video upload kar sakta hai.")
‎        return
‎
‎    # Simple link check
‎    if text.startswith("http://") or text.startswith("https://"):
‎        VIDEOS.append(text)
‎        await update.message.reply_text("✅ Video upload ho gayi!")
‎    else:
‎        await update.message.reply_text("❌ Sirf valid video link bhejein.")
‎
‎# ===============================
‎# MAIN
‎# ===============================
‎if __name__ == "__main__":
‎    app = ApplicationBuilder().token(BOT_TOKEN).build()
‎
‎    # Handlers
‎    app.add_handler(CommandHandler("start", start))
‎    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, upload_video))
‎
‎    print("Bot running...")
‎    app.run_polling()
‎