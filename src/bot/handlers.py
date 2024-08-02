import requests
from telegram import Update
from telegram.ext import ContextTypes


def handle_response(text: str) -> str:
    global user_job_title

    if text not in ["no", "yes"]:
        user_job_title = text
    return text


user_job_title = ""


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text.lower()

    print(f"user {update.message.chat.id} in {user_job_title}: {text} ")

    handle_response(text)

    if text == "yes" and user_job_title != "":
        await update.message.reply_text(
            f"looking for {user_job_title} job offers for you."
        )
        print("start")
        results = requests.get(
            "https://github.com/",
            # proxies={"http": "45.131.4.71:80"},
        )
        print(results)
        # for page in results:
        #     for job in page:
        #         await update.message.reply_text(
        #             f"{job.title}, {job.city}, {job.passed_days}"
        #         )
    elif text == "no":
        handle_response("")
        await update.message.reply_text(f"type your job title again.")
    else:
        response_text = f"Are you looking for {user_job_title} jobs? answer yes or no."
        await update.message.reply_text(response_text)
