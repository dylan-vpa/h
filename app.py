from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of translations for "Hannah, I love you" in many world languages
translations = [
    {"language": "Spanish", "message": "Hannah, te amo"},
    {"language": "English", "message": "Hannah, I love you"},
    {"language": "French", "message": "Hannah, je t'aime"},
    {"language": "Italian", "message": "Hannah, ti amo"},
    {"language": "German", "message": "Hannah, ich liebe dich"},
    {"language": "Portuguese", "message": "Hannah, eu te amo"},
    {"language": "Japanese", "message": "ハンナ、愛してる (Hanna, aishiteru)"},
    {"language": "Korean", "message": "한나, 사랑해 (Hanna, saranghae)"},
    {"language": "Russian", "message": "Ханна, я тебя люблю (Khanna, ya tebya lyublyu)"},
    {"language": "Arabic", "message": "هانا، أحبك (Hana, uḥibbuk)"},
    {"language": "Mandarin Chinese", "message": "汉娜，我爱你 (Hànnà, wǒ ài nǐ)"},
    {"language": "Hindi", "message": "हन्ना, मैं तुमसे प्यार करता हूँ (Hanna, main tumse pyar karta hoon)"},
    {"language": "Bengali", "message": "হান্না, আমি তোমাকে ভালোবাসি (Hanna, āmi tōmāke bhālōbāsi)"},
    {"language": "Urdu", "message": "ہننا، میں تم سے پیار کرتا ہوں (Hanna, main tumse pyar karta hoon)"},
    {"language": "Swahili", "message": "Hannah, nakupenda"},
    {"language": "Turkish", "message": "Hannah, seni seviyorum"},
    {"language": "Dutch", "message": "Hannah, ik hou van je"},
    {"language": "Polish", "message": "Hannah, kocham cię"},
    {"language": "Greek", "message": "Χάνα, σ' αγαπώ (Hána, s' agapó)"},
    {"language": "Thai", "message": "ฮันนาห์ ฉันรักคุณ (Hanna, chan rak khun)"},
    {"language": "Vietnamese", "message": "Hannah, anh yêu em"},
    {"language": "Hebrew", "message": "חנה, אני אוהב אותך (Hana, ani ohev otach)"},
    {"language": "Persian", "message": "هانا، دوستت دارم (Hana, dustet daram)"},
    {"language": "Tamil", "message": "ஹன்னா, நான் உன்னை காதலிக்கிறேன் (Hanna, nān unnai kādalikkiṟēn)"},
    {"language": "Telugu", "message": "హన్నా, నీవు నాకు ఇష్టం (Hanna, nīvu nāku iṣṭaṁ)"},
    {"language": "Malayalam", "message": "ഹന്ന, ഞാൻ നിന്നെ സ്നേഹിക്കുന്നു (Hanna, ñān ninne snēhikkunnu)"},
    {"language": "Punjabi", "message": "ਹੰਨਾ, ਮੈਂ ਤੁਹਾਨੂੰ ਪਿਆਰ ਕਰਦਾ ਹਾਂ (Hanna, main tuhānū piāra karadā hāṁ)"},
    {"language": "Gujarati", "message": "હેન્ના, હું તને પ્રેમ કરું છું (Hanna, huṁ tane prēma karuṁ chuṁ)"},
    {"language": "Marathi", "message": "हन्ना, मी तुझ्यावर प्रेम करतो (Hanna, mī tujhyāvara prēma karatō)"},
    {"language": "Kannada", "message": "ಹನ್ನಾ, ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ (Hanna, nānu ninnannu prītisuttēne)"},
    {"language": "Burmese", "message": "ဟန်နာ၊ ငါမင်းကိုချစ်တယ် (Hanna, nga min go chit te)"},
    {"language": "Indonesian", "message": "Hannah, aku mencintaimu"},
    {"language": "Malay", "message": "Hannah, saya sayang awak"},
    {"language": "Filipino (Tagalog)", "message": "Hannah, mahal kita"},
    {"language": "Yoruba", "message": "Hannah, mo nifẹ rẹ"},
    {"language": "Hausa", "message": "Hannah, ina son ki"},
    {"language": "Igbo", "message": "Hannah, a hụrụ m gị n'anya"},
    {"language": "Amharic", "message": "ሃና፣ እወድሻለሁ (Hana, iwedishalehu)"},
    {"language": "Zulu", "message": "Hannah, ngiyakuthanda"},
    {"language": "Shona", "message": "Hannah, ndinokuda"},
    {"language": "Somali", "message": "Hannah, waan ku jeclahay"},
    {"language": "Nepali", "message": "हन्ना, म तिमीलाई माया गर्छु (Hanna, ma timīlāī māyā garchu)"},
    {"language": "Sinhala", "message": "හැනා, මම ඔයාට ආදරෙයි (Hænā, mama oyāṭa ādareyi)"},
    {"language": "Khmer", "message": "ហាន់ណា ខ្ញុំស្រឡាញ់អ្នក (Hanna, khnhom sralanh anak)"},
    {"language": "Lao", "message": "ຮັນນາ, ຂ້ອຍຮັກເຈົ້າ (Hanna, khoy hak chao)"},
    {"language": "Mongolian", "message": "Ханна, би чамайг хайрладаг (Hanna, bi chamaig khairladag)"},
    {"language": "Tibetan", "message": "ཧན་ན། ང་ཁྱོད་ལ་གཅེས། (Hanna, nga khyod la gces)"},
    {"language": "Albanian", "message": "Hannah, të dua"},
    {"language": "Armenian", "message": "Հաննա, ես քեզ սիրում եմ (Hanna, yes k’ez sirum yem)"},
    {"language": "Azerbaijani", "message": "Hannah, səni sevirəm"},
    {"language": "Basque", "message": "Hannah, maite zaitut"},
    {"language": "Belarusian", "message": "Ханна, я цябе кахаю (Khanna, ya tsiabe kakhayu)"},
    {"language": "Bosnian", "message": "Hannah, volim te"},
    {"language": "Bulgarian", "message": "Хана, обичам те (Hana, obicham te)"},
    {"language": "Catalan", "message": "Hannah, t'estimo"},
    {"language": "Croatian", "message": "Hannah, volim te"},
    {"language": "Czech", "message": "Hannah, miluji tě"},
    {"language": "Danish", "message": "Hannah, jeg elsker dig"},
    {"language": "Estonian", "message": "Hannah, ma armastan sind"},
    {"language": "Finnish", "message": "Hannah, rakastan sinua"},
    {"language": "Georgian", "message": "ჰანა, მიყვარხარ (Hana, miq’varkhar)"},
    {"language": "Hungarian", "message": "Hannah, szeretlek"},
    {"language": "Icelandic", "message": "Hannah, ég elska þig"},
    {"language": "Irish", "message": "Hannah, is breá liom tú"},
    {"language": "Latvian", "message": "Hannah, es tevi mīlu"},
    {"language": "Lithuanian", "message": "Hannah, aš tave myliu"},
    {"language": "Macedonian", "message": "Хана, те сакам (Hana, te sakam)"},
    {"language": "Maltese", "message": "Hannah, inħobbok"},
    {"language": "Norwegian", "message": "Hannah, jeg elsker deg"},
    {"language": "Romanian", "message": "Hannah, te iubesc"},
    {"language": "Serbian", "message": "Хана, волим те (Hana, volim te)"},
    {"language": "Slovak", "message": "Hannah, ľúbim ťa"},
    {"language": "Slovenian", "message": "Hannah, ljubim te"},
    {"language": "Swedish", "message": "Hannah, jag älskar dig"},
    {"language": "Ukrainian", "message": "Ханна, я тебе кохаю (Khanna, ya tebe kokhayu)"},
    {"language": "Welsh", "message": "Hannah, rwy'n dy garu"}
]

# Counter to cycle through translations
current_index = 0

@app.route('/')
def love_message():
    global current_index
    # Get the current translation
    translation = translations[current_index]
    # Increment index, loop back to 0 if at the end
    current_index = (current_index + 1) % len(translations)
    return jsonify({
        'language': translation['language'],
        'message': translation['message']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1612, debug=True)
