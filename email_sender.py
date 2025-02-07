from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import base64
import os

# Scope yang dibutuhkan untuk mengirim email
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate():
    """Autentikasi ke Gmail API"""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def send_email(to_email, subject, body, attachment_path=None):
    """Mengirim email dengan atau tanpa attachment"""
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)

    message = MIMEMultipart()
    message['to'] = to_email
    message['subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Menambahkan attachment jika ada
    if attachment_path:
        attachment_filename = os.path.basename(attachment_path)
        with open(attachment_path, 'rb') as attachment_file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(attachment_file.read())
        base64.encodebytes(attachment.get_payload(decode=True))
 # Encode attachment
        attachment.add_header('Content-Disposition', f'attachment; filename="{attachment_filename}"')
        message.attach(attachment)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message_data = {'raw': raw_message}

    try:
        service.users().messages().send(userId="me", body=message_data).execute()
        print(f"Email terkirim ke {to_email}")
    except Exception as e:
        print(f"Error: {e}")

# Contoh penggunaan: Kirim email ke banyak penerima dengan attachment
recipients = ["grizeldaagatha@gmail.com", "dianastutik728@gmail.com", "fararista08@gmail.com", "firdakunyel01539@gmail.com", "adipratamablitar20@gmail.com", "andahonnors@gmail.com", "squidwardgaming2@gmail.com", "tanalurifqi@gmail.com", "ardinfaizal947@gmail.com", "mochammad.rizki3107@sma.belajar.id", "kii802875@gmail.com", "fauzanaalfito@gmail.com", "mialinda10506@gmail.com", "umi.jamilatun52@sma.belajar.id", "latifatulagustina93@gmail.com", "vellayuliani07@gmail.com", "agneskonexx@gmail.com", "febi.anti40@sma.belajar.id", "anisabinti30@gmail.com", "titan.vicne28@sma.belajar.id", "saniandani6@gmail.com", "anggaramlbb2@gmail.com", "rafiiiabraham@gmail.com", "fahreza8988@gmail.com", "nurhusen723@gmail.com", "kuswiyantokuswiyanto83@gmail.com", "bagus.setiyawan631@sma.belajar.id", "balqisvinolia@gmail.com", "hanaalyaaatul@gmail.com", "rianur280107@gmail.com", "siti.ro314@sma.belajar.id", "pandaianak21@gmail.com", "fara.nadia268@sma.belajar.id", "luispebriani@gmail.com", "anisa.yulianti1075@sma.belajar.id", "sucinangimuljanna@gmail.com", "riskanovia54@gmail.com", "zasfadhilatul99@gmail.com", "nurizaaprilianti21@gmail.com", "deafaniputri79@gmail.com", "sindikartika107@gmail.com", "zarinainatsasily@gmail.com", "jesika.isma21@sma.belajar.id", "nurjanah3125@gmail.com", "pinasarum256@gmail.com", "anif9398@gmail.com", "nikmahfilaily@gmail.com", "vvivi8326@gmail.com", "fazura.eva20@gmail.com", "zosomyemouza88@gmail.com", "rezadibule@gmail.com", "adityakusumaw36@gmail.com", "jonataedo47@gmail.com", "rasyazidan564@gmail.com", "andra818173@gmail.com", "linayunita1286@gmail.com", "dwiranggadimas70@gmail.com", "aadauliah5@gmail.com", "sekar.ayu30684@sma.belajar.id", "ichayustina03@gmail.com", "fifin9502@gmail.com", "septiaaina72@gmail.com", "meilinalestari199@gmail.com", "divaslselsy@gmail.com", "dytacandrakirana@gmail.com", "ivandani540@gmail.com", "zaskiap090@gmail.com", "andirarahma13@gmail.com", "wulantiwi585@gmail.com", "vitaalifa510@gmail.com", "dewinurlitasari61@gmail.com", "youzyyy20@gmail.com", "rendyandriansyah241@gmail.com", "olivianovitasari065@gmail.com", "rinarahmaw04@gmail.com", "dilalutfy9@gmail.com", "nikadifa01@gmail.com", "nazala.firdausi131@gmail.com", "andhiniw19@gmail.com", "zumrotul.azizah95@sma.belajar.id", "mailamafza@gmail.com", "diohanggara31@gmail.com", "irenkamila476@gmail.com", "isjihar.fajariyah2@sma.belajar.id", "rafayuvella@gmail.com", "afristawulandaridefi@gmail.com", "floraphone317@gmail.com", "ameliaputri73472@gmail.com", "ratnasaputri426@gmail.com", "sigitirawan2805@gmail.com", "adelia.rmadni69@gmail.com", "lutfin042@gmail.com", "mohammadarifwahyu23@gmail.com", "syfaanaacan@gmail.com", "nandarnv41@gmail.com", "dindahidayah22@gmail.com", "kholiliqwerty45@gmail.com", "ismidaggraini02@gmail.com", "rindapurnaning@gmail.com", "muson368@gmail.com", "finapuspitanurlaili29@gmail.com", "rikarokani6@gmail.com", "devinur269@gmail.com", "dellaayu.0411@gmail.com", "rarauli.angxra@gmail.com", "awaryzx@gmail.com", "andriantricahya06@gmail.com", "maylahaniyah2@gmail.com", "alfathahmad565@gmail.com", "irafatma894@gmail.com", "tiaralestariyy@gmail.com", "umiaidah736@gmail.com", "da0037286@gmail.com", "panjikalyana@gmail.com", "julia.asna27@sma.belajar.id", "cindynovieta1@gmail.com", "nailarahma619@gmail.com", "nillaapre@gmail.com", "aiccunggg@gmail.com", "erlanggarehan62@gmail.com", "rahmaanilha@gmail.com", "anggunfitriaaa19@gmail.com", "sssbilaaa@gmail.com", "jeynisvalesiva@gmail.com", "ekarisky49@gmail.com", "dewimahardika94@gmail.com", "nadilanurul36@gmail.com", "anjarnastiti02@gmail.com", "aayu7015@gmail.com", "rnaditama78@gmail.com", "duwinovita139@gmail.com", "fatmafitriasari26@gmail.com", "linggadisavon8@gmail.com", "raffyatha2010@gmail.com", "renatashe07@gmail.com", "alexaxa509@gmail.com", "dhita14rahmaputri@gmail.com", "nadiaw307@gmail.com", "enakmasakan79@gmail.com", "latifaacntik@gmail.com", "agneschelfar@gmail.com", "ivanrifai783@gmail.com", "am8691499@gmail.com", "citrabintang654@gmail.com", "dwfriskaa@gmail.com", "novetasha202@gmail.com", "lalasaja025@gmail.com", "diahwidya015@gmail.com", "ndotoi8@gmail.com", "gita15052006@gmail.com", "ardyhisam174@gmail.com", "putridevita31523@gmail.com", "andikataufani3@gmail.com", "ztrihandika@gmail.com", "nadzifahasnaaa@gmail.com", "serlindaserli3@gmail.com", "naylawz12@gmail.com", "mochamadahmad59@gmail.com", "ahmadrifai4012@gmail.com", "tisyariskin@gmail.com", "ridwan.ardiansah310@sma.belajar.id", "setiamaharani4@gmail.com", "kurniaandika997@gmail.com", "yakymuhammad26@gmail.com", "nandasiska528@gmail.com", "01silmi.nasrumillah@gmail.com", "sherly.dwi2083@sma.belajar.id", "ivanabdypratama53@gmail.com", "asmaulnurulkhotimah@gmail.com", "dwil18058@gmail.com", "ayubilqis692@gmail.com", "nabilasarah633@gmail.com", "fauziah5lutfi@gmail.com", "teguhprayogo920@gmail.com", "adeliachelsea08@gmail.com", "zulfikarfauzi07@gmail.com", "alwasikn@gmail.com", "desinurnatalia72@gmail.com", "fyanuarputra@gmail.com", "ambarwati15188@gmail.com", "fitriameeei25@gmail.com", "dheamaheswari123@gmail.com", "shellyrahmawati348@gmail.com", "dewiragil611@gmail.com", "sdedy1702@gmail.com", "ungainlycraving73@gmail.com", "revaliapratama210@gmail.com", "arkhanradhis@gmail.com", "fyndavabellia@gmail.com", "adhiyatihani@gmail.com", "zulanticharahma@gmail.com", "fibrisani@gmail.com", "safrianinasution14@gmail.com", "pa089669@gmail.com", "sabrinafadhilah25@gmail.com", "habsyfaizil02@gmail.com", "fa7028797@gmail.com", "jhejian12@gmail.com", "hengkipeasetyo@gmail.com", "afibdwiuswatun@gmail.com", "ymnayraa@gmail.com", "elsa29011@gmail.com", "zanuarihsan10@gmail.com"]

for email in recipients:
    subject = "Proposal Kerjasama – Manufaktur Pakaian Premium oleh GOD'S STATE"
    body = """Kepada Klien,

Saya harap email ini menemui Anda dalam keadaan baik.

Perkenalkan, nama saya Yosa, saya mewakili GOD'S STATE, mitra terpercaya dalam manufaktur pakaian premium. Kami juga mengkhususkan diri dalam pembuatan seragam dan pakaian korporat berkualitas tinggi yang mencerminkan identitas dan nilai-nilai brand Anda.

Kami memahami bahwa seragam bukan sekadar pakaian—melainkan representasi dari cerita, kebanggaan, dan identitas Anda. Dengan keahlian kami, bahan baku premium, serta layanan end-to-end, kami siap membantu Anda menciptakan seragam yang memberikan kesan mendalam.

Terlampir dalam email ini, Anda akan menemukan Proposal Kerjasama kami, yang mencakup:
- Latar belakang dan pengalaman kami.
- Produk yang kami tawarkan serta keunggulan kompetitif kami.
- Testimoni dari klien kami yang puas.
- Penjelasan detail mengenai proses kerjasama kami.

Kami sangat senang jika ada kesempatan untuk berdiskusi lebih lanjut mengenai kebutuhan spesifik Anda dan memberikan solusi yang sesuai untuk organisasi Anda. Silakan hubungi saya langsung via WhatsApp di +62 895-8072-94100 (Yosa) atau email ke gods.state.business@gmail.com untuk menjadwalkan konsultasi atau meminta informasi lebih lanjut.

Terima kasih telah mempertimbangkan GOD'S STATE sebagai mitra Anda. Kami menantikan kesempatan untuk bekerja sama dan membantu mewujudkan visi Anda.

Salam hormat,
Yosa
WhatsApp: +62 895-8072-94100 (Yosa)
Email: gods.state.business@gmail.com
"""
    attachment = "gstprop.docx"  # Ganti dengan nama file yang ingin dikirim

    send_email(email, subject, body, attachment)