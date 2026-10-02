"""
Word lists used by detect_language.py. Edit freely: one word per entry, lower case.

ROMAN_MARKERS  words that, written in Latin letters, show the review is in an Indian language
               (romanized Hindi, Marathi, ...). A word may appear under several languages.
               Only words that are not also everyday English words belong here.
ENGLISH_EXTRA  English spellings common in Indian reviews that a dictionary does not know
               (gud, nyc, osm, plz ...) and farm words such as urea or npk.
NEUTRAL        words that say nothing about the language: app and brand names, crop names
               used in both English and Indian-language reviews.
DEVANAGARI_*   words that separate Marathi from Hindi when the review is in Devanagari and the
               IndicLID model is not installed.
"""

def _w(s):
    return set(s.split())


ROMAN_MARKERS = {
    "hin": _w("""
        hai hain hae nahi nahin nhi nahee nai bahut bahot bohot bohut bhut bhot bht bahuut
        accha acha achha achcha acchha acchi achhi achi acche achhe kya kyu kyun kyon kyunki kyuki kyoki kyonki
        kaise kese kaisa kaisi kaun kahan kidhar mujhe mujhko mera meri hame hamein humein hamara hamari
        hamare humko hamko aapka aapki aapke apka apki apke aapko apko aapne tumhara tumhari tumhe aur bhi sabhi
        sabko sabse raha rha rahi rhi rahe rhe rahta rehta rehti karo karna karne karta karte karti kiya kiye
        kijiye kariye karein krna krne krta krte krti kro kia gaya gya gayi gyi gaye gye hogaya hogya hojata
        hojati diya diye dia dijiye dena dene deta dete deti liya liye lia lena lene leta lete hota hoti hote
        hona hone hoga hogi honge milta milti milte mila mili milega milegi chahiye chaiye chahie chahte chahta
        chahti lagta lagti lagte sakta sakti sakte isme ismein isse isko iska iski iske usme usse usko uska uski
        uske unka unki unke unko inka inki inke wala wali wale waala waali waale abhi kabhi jabhi tabhi phir fir
        bilkul sirf keval kewal saath bina kuch kuchh kisi kisko bekar bekaar bakwas bakwaas faltu faaltu ghatiya
        ghatia badiya badhiya badiyaa bdiya bdhiya behtar behtareen behtarin shandar shaandar zabardast jabardast
        kamaal ekdum ekdam jankari jaankari jaankaari madad sahayata upyogi upyogee labh labhdayak fayda faida
        faydemand dhanyawad dhanyavad dhanywad shukriya sukriya kisan kisano kisanon kisaan kheti kheton 
        fasalon beej beejon khad dawai dawaiyan mitti mausam baarish barish sinchai sarkar sarkari yojana yojna
        paisa paise rupaye rupay rupye wapas vapas wapis kripya krpya kirpya kripa samasya samadhan sahi galat
        theek thik thek jaldi samay bhaiyo bhaiyon bhaiya behan didi lekin magar agar warna varna isliye toh
        gaon gaanv batao bataye bataiye bataen samajh samjha samjhe samjhaya pata pta maloom malum dikhta dikhti
        dikhai dikhaye khulta khulti khulega chalta chalti chalega jai bhav daam keemat kimat andar bahar khud
        hamesha humesha zyada jyada kaam chalu bandh dhoka dhokha chor vishwas bharosa suvidha jaise waise vaise
        aise aisa aisi waisa tha thi hoon haan aaya mast khoob bhai kaafi kafi mujhse humse aapse naya nayi naye
        purana purani vala vali vale kar maza maja
        tamatar paudha paudhe paudhon keeda keede kide rog bimari beemari upaj utpadan khaad kapas gehu gehun
        chawal sarson ganna aloo pyaz pyaaj mirch makka lahsun adrak phal phool patti pattiyan jadon khet kheton
        pani chhidkav chidkav keetnashak kitnashak kharpatwar barsat garmi sardi thand dhoop rakhe rakho dekho dekha dekhiye dekhe
    """),
    "mar": _w("""
        aahe ahe ahet aahet nahi naahi nahiye khup khupach khoop chan chhan chaan chhaan changla changle changli
        bhari bhaari jhakas zakas mast mala malaa amhala aamhala amhi aamhi tumhi tumhala aapan apan majha maza
        majhi mazi majhe  tumcha tumchi tumche tumchya tyacha tyachi tyanchi tyancha aaplya aplya apla aapla
        apli aapli aaple aple shetkari shetkaryansathi shetkaryanna shetkaryana shetkaryanchya sheti shetat kara
        karave karava kele keli kela kelay kelyavar karun karto kartat hote hota hoti ani aani kay kaay kahi
        kahich kontya konti kuthe kevha kasa kashi kase sathi saathi madhe madhye mdhe madhun zala jhala zali
        jhali zale jhale zalay jhalay barobar uttam mahiti upyukt upayukt upyogi dhanyavad dhanyawad nako nko
        pahije pahijet milte milat milali milala milel ghya ghyave dya dyave sanga sangitle sangitla sangave ata
        aata udya lavkar lavkarach paus paaus havaman havamaan pik pike pikanchi pikache aushadh fawarni favarni
        bajarbhav bajar bhav dada bhau saheb mitra kanda lagvad lagwad kapus harbhara gahu jwari bajri dalimb
        draksha vangi bhuimug kandyachi alya alyamule pani
    """),
    "guj": _w("""
        che chhe chhu chho saru saras sars saaru maja majja majaa khub bahu nathi nathe kem tame tamne tamaru
        amne amaru maate khedut khedu mahiti upyogi joie joiye joiae hatu hati hata thay thayu thase
        karvu karvanu karjo karso aavu aavi aave gamyu gamiyu gami abhar aabhar vadhare vadhu ochhu ochu jordar kai
    """),
    "pan": _w("""
        vadiya wadiya vadhia vadhiya wadhiya vdia vadia changa changi haan tusi tuhanu tuhada tuhadi tuhade sanu
        saanu asi assi sadda saddi kaafi paji paaji naal vich vicho hunda hundi hunde karda kardi karde
        kitta kisaan dhanwad dhanvaad mehrbani meharbani rabb waheguru aaya
    """),
    "ben": _w("""
        khub bhalo valo bhaloi onek ami amar amra amader tumi tomar apni apnar apnader kintu hoy hoyna hoye
        hoyeche hocche hochhe achhe nei kore korte korche korben korun kemon kothay dhonnobad dhanyabad sundor
        chasi chashi krishok kaj kaaj jonno jonne theke niye holo hobe dorkar darkar kharap kharaap
    """),
    "tam": _w("""
        nalla nallaa nallathu nalladhu romba rombha rombo irukku iruku irukkum illa illai enna ennaku enaku
        vendum venum venam panna pannunga pannanum panrom nandri nanri sema semma vivasayi vivasayam vivasayigal
        theriyala theriyum puriyala puriyuthu ungal unga enga engal naan neenga neengal appo ippo ippa inga anga
        epdi eppadi epadi sollunga solla vanga vaanga varala varuthu kudukka kodunga payan payanulla payanullathu
        arumai arputham mokka
    """),
    "tel": _w("""
        chala chaala bagundi baagundi bagunna bagundhi bagunnadi ledu ledhu undi undhi emaina meeru meru
        manchi raithu rythu raithulu rythulu dhanyavadalu andi kuda kosam vachindi ravatledu cheyandi cheyyali
        chesi chesina chesaru nenu naaku maaku memu enti avunu kaadu kani istam ishtam upayogam upayogakaram
    """),
    "kan": _w("""
        tumba thumba chennagide chanagide chennagi chennag olle olleya ollethu upayuktha upayukta sakkath sakath
        sakkat nimma nimmage namma nammage maadi madi agide aagide aagilla agilla beku bekagide illa idhe
        kelsa kelasa raitha raitharu raitharige dhanyavadagalu dhanyavaadagalu haage aadre adre yenu yaake hege
        hegide banni baralla sigutte sigatte kodi ondu
    """),
    "mal": _w("""
        nalla valare undu aanu ente enthu ningal ningalude nanni kollam adipoli karshakar karshakan upakarapradam
        upakaram kure kurachu ishtapettu pakshe onnum onnumilla cheyyan cheyyunnu venam sheri kittunnilla kitti
        kittum mikacha mikachathu polichu kidu kidilam kidilan illa
    """),
    "ori": _w("""
        bhala bahuta khub kana ame amara apana apananka dhanyabad chasi chasa heba hela kariba karibaku karantu
        darkar sundara upakari ebe emiti kemiti kouthi sabu
    """),
    "asm": _w("""
        bhal bhaal khub ase aase moi mok apuni apunar amak dhonyobad kintu hol hoise hobo korok kori krishok
        bohut xokolo sokolu nai
    """),
}

# Order used to break ties between languages with the same number of marker words
LANG_PRIORITY = ["hin", "mar", "guj", "pan", "ben", "tam", "tel", "kan", "mal", "ori", "asm"]

ENGLISH_EXTRA = _w("""
    ok okk okay gd gud good gooood nyc nic nyce nycc osm osum awsm awsome awesm awsum osam thnx thnks thanx
    thx tnx thanku thanq thankyou plz pls plzz plzzz gr8 vry bst superb supb xlnt exlnt excelent exellent
    excellant woww wow app apps frnd frnds msg info govt pvt dept qty otp upi kyc pdf
    urea dap npk mop ssp zinc sulphur boron pesticide pesticides insecticide insecticides fungicide fungicides
    herbicide herbicides weedicide weedicides agronomist agronomists agri agro agritech paddy groundnut
    soyabean soybean brinjal chilli chili okra sugarcane drip sprinkler rotavator harvester thresher
    cultivator sprayer drone drones fertiliser fertilisers fertilizer fertilizers
""")

NEUTRAL = _w("""
    agrostar dehaat bighaat gramophone bharatagri agribegri agriapp krishify plantix kissanai kisankraft
    agricentral ninjacart agribazaar animall dvara surabhi aquaconnect drgrow tractorjunction khetigaadi fyllo
    aquaexchange farmonaut farmrise nurture krishe itcmaars maars jiokrishi jio amul meghdoot sarathi enam
    uzhavan kathir mahavistaar vistaar pmkisan pmfby cottonace salam grainbank ergos mygromor gromor ecotron
    ecozen cropwise syngenta upaj iffco playstore paytm phonepe gpay whatsapp youtube mahindra bayer
    jowar bajra tur toor moong urad chana arhar masoor bhindi lauki karela methi palak jeera haldi mirchi
    mandi ji sir madam mam aap aapp
""")

# Devanagari: words typical of Marathi vs Hindi (fallback when the IndicLID model is not installed)
DEVANAGARI_MARATHI = set("""
    आहे आहेत नाही खूप खूपच छान मला आम्हाला आम्ही तुम्ही आणि करा केले केली झाले झाला झाली साठी मध्ये होते
    आपल्या माहिती शेतकरी शेतकऱ्यांसाठी शेतकऱ्यांना शेती पाहिजे मिळाले मिळते चांगले चांगली उपयुक्त बरोबर
    काय कसे कधी आता द्या घ्या नको तुमचे आमचे माझे माझा माझी ॲप ॲप्लिकेशन
""".split())
DEVANAGARI_HINDI = set("""
    है हैं नहीं बहुत अच्छा अच्छी अच्छे और में का की के को से किसान किसानों लिए यह ये वह मुझे मेरा हम आप
    बढ़िया बेकार जानकारी मदद उपयोगी खेती फसल रहा रही रहे गया गई दिया किया कर करें करता होता होती चाहिए
    ऐप एप
""".split())
