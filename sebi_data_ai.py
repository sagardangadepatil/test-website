import fitz  # PyMuPDF

def extract_pdf_text(pdf_url):
    response = requests.get(pdf_url)
    with open("temp.pdf", "wb") as f:
        f.write(response.content)

    doc = fitz.open("temp.pdf")
    text = "\n".join([page.get_text() for page in doc])
    return text

def summarize(text):
    prompt = f"Summarize this SEBI disclosure in 3 lines:\n\n{text[:3000]}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def summarize(text):
    prompt = f"Summarize this SEBI disclosure in 3 lines:\n\n{text[:3000]}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

from twilio.rest import Client

def send_whatsapp_message(summary, link, to="+919503919180"):
    client = Client("TWILIO_SID", "TWILIO_AUTH")
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        to=f"whatsapp:{to}",
        body=f"📢 New SEBI Disclosure:\n\n{summary}\n\n📄 Full PDF: {link}"
    )
    return message.sid
