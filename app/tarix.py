import random

# Savollar ro'yxati va ularning variantlari
questions = [
    {
        "question": "Mustaqillik qo’lga kiritilgunga qadar O‘zbekiston tarixi eng qadimgi davrdan boshlab nechta taraqqiyot bosqichiga bo’lingan edi ?",
        "options": ["3 ta", "5ta", "2 ta", "4 ta"],
        "answer": "5ta"
    },
    {
        "question": "Tariximizning yozuvsiz zamonlarga oid davrini o‘rganishda qaysi manbalar yordamga keladi ?",
        "options": ["Moddiy va yozma manbalar", "Yozma va arxiv manbalari", "Arxeologik va yozma manbalar", "Arxeologik, antropologik va etnografik manbalar"],
        "answer": "Arxeologik, antropologik va etnografik manbalar"
    },
    {
        "question": "Quyidagi javoblar ichidan O‘zbekiston tarixi fanining ilmiy-nazariy uslublari va tamoyillari to’g’ri keltirilgan javobini toping ?",
        "options": ["Tarixiy hodisa va voqealarni, hujjat va faktlarni ilmiy, xolisona o‘rganish va tahlil qilish", "Tarixni milliylik va umuminsoniylik asosida o‘rganish va tahlil qilish", "Tarixni haqqoniy, tarixiy-falsafiy mantiqiylik asosida o‘rganish va yozish", "Barcha javoblar to’g’ri"],
        "answer": "Barcha javoblar to’g’ri"
    },
    {
        "question": "Nima sababdan O‘zbekiston tarixi fanini o’rganishda tarixiy manbalarning o‘rni va ahamiyati kata ?",
        "options": ["Manbalar tarixni tilga kiritadi", "Haqqoniy tarix faqatgina yozma manbalarda yozib qoldirilgan", "Inson qo’li va aql-zakovati bilan yaratilganligi uchun", "To’g’ri javob yo’q"],
        "answer": "Manbalar tarixni tilga kiritadi"
    },
    {
        "question": "Manbalar o‘z holatiga ko‘ra qanday ko‘rinishlarga ega bo‘ladi ?",
        "options": ["Arxeologik va moddiy", "Yozma va moddiy", "Etnografik va moddiy-ashyoviy", "Yozma va arxiv manbalari"],
        "answer": "Yozma va moddiy"
    },
    {
        "question": "Birlamchi manbaga nimalar kiradi ?",
        "options": ["Moddiy manbalar", "Yozma manbalar", "Tarixiy hujjatlarning asl nusxasi", "Kitoblar va adabiyotlar"],
        "answer": "Tarixiy hujjatlarning asl nusxasi"
    },
    {
        "question": "Quyidagi javoblarning qaysi birida “O‘zbekistonning eng yangi tarixi” fanini o‘qitishning maqsadi to’g’ri keltirilgan ?",
        "options": ["Mustaqillik yillarida O‘zbekiston Respublikasida yuz bergan muhim o‘zgarishlarni anglatish", "Amalga oshirilayotgan tub islohotlarning mazmun-mohiyatini ko‘rsatish", "Jamiyat hayotida aholining, jumladan, talaba-yoshlarning o‘rnini, o‘zligini anglatish", "Barcha javoblar to’g’ri"],
        "answer": "Barcha javoblar to’g’ri"
    },
    {
        "question": "O‘zbekiston Respublikasida yoshlarning ijtimoiy-iqtisodiy, siyosiy va huquqiy kafolatlari qaysi qonunda  belgilab qo‘yilgan ?",
        "options": ["”Ta’lim to’g’risida”gi qonunda", "”Kadrlar tayyorlash milliy dasturi”da", "“O‘zbekistonda yoshlarga oid davlat siyosatining asoslari to‘g‘risida”gi qonunida", "“Yoshlar to’g’risida”gi qonunda"],
        "answer": "“O‘zbekistonda yoshlarga oid davlat siyosatining asoslari to‘g‘risida”gi qonunida"
    },
    {
        "question": "O‘zbekiston Respublikasi Prezidenti Shavkat Mirziyoyev 2017-yil 27-mart sanasida mamlakat taraqqiyoti yo‘lida fidokorona xizmat qilgan qaysi atoqli davlat arbobi xotirasini ulug‘lash maqsadida ushbu shaxs tavalludining 100 yilligini nishonlash to‘g‘risidagi qarorga imzo chekkan edi ?",
        "options": ["Ozod Sharafiddinov", "Sharof Rashidov", "Jaloliddin Manguberdi", "Amir Temur"],
        "answer": "Sharof Rashidov"
    },
    {
        "question": "O’zbekiston Respublikasida yoshlarning aholi tarkibidagi salmog‘i to’g’ri keltirilgan javobni toping ?",
        "options": ["50 foiz", "50 foizdan yuqori", "60 foizdan yuqori", "70 foiz"],
        "answer": "60 foizdan yuqori"
    },
    {
        "question": "1946-1947 oquv yilda yurtimizda nechta maktab bor edi ?",
        "options": ["9188 ta", "9716 ta", "4483 ta", "9256 ta"],
        "answer": "4483 ta"
    },
    {
        "question": "“Qayta qurish” siyosati qachondan boshlandi ?",
        "options": ["1985 yil SSSR Kommunistik partiyasi MQ ning 23-aprеl  plеnumidan so’ng", "1989 yil SSSR Kommunistik partiyasi MQ ning XXV s'еzdidan so’ng", "1990 yil mustaqillik dеklaratsiyasi qabul qilingandan so’ng", "1980-1985 yillarda M.S.Gorbachеv boshchiligida"],
        "answer": "1985 yil SSSR Kommunistik partiyasi MQ ning 23-aprеl  plеnumidan so’ng"
    },
    {
        "question": "Islom Abdug‘anievich Karimov O‘zbekistonning birinchi rahbari sifatida o‘z faoliyatini qachondan boshladi ?",
        "options": ["1989-yil 23-iyunda", "1990-yil 20-iyunda", "1991-yil 1-sentabrda", "1989-yil 20-oktyabrda"],
        "answer": "1989-yil 23-iyunda"
    },
    {
        "question": "Mustaqillik arafasida sobiq ittifoqda (Markaz) bo’lib o’tgan davlat to’ntarishlari bo’lib o’tgan sanani ko’rsating ?",
        "options": ["1991-yil 19-avgust kuni", "1989-yil may-iyun kunlari", "1985-yil aprelida", "1991-yil 19-21 avgust kunlari"],
        "answer": "1991-yil 19-21 avgust kunlari"
    },
    {
        "question": "O’tkir Hoshimovning qaysi asarida afg’on urushining oqibatlari ko’rsatib berilgan ?",
        "options": ["Tushda kechgan umrlar", "Nur borki, soya bor", "Ikki eshik orasi", "Afg’on shamoli"],
        "answer": "Afg’on shamoli"
    },
    {
        "question": "Markaz tomonidan uyushtirilgan “o‘zbeklar ishi”, “paxta ishi” qachon boshlandi ?",
        "options": ["XX asring 90-yillariga", "XX asring 80 yillariga", "1985-1990 yillariga", "1985-1990 yillariga"],
        "answer": "XX asring 80 yillariga"
    },
    {
        "question": "1979-1989-yillarda bo’lib o’tgan “Afg’on urushi”da qancha o’zbekistonlik jangchi ishtirok etgan ?",
        "options": ["65 mingdan ortiq", "45 mingdan ortiq", "55 mingdan ortiq", "100 mingdan ortiq"],
        "answer": "65 mingdan ortiq"
    },
    {
        "question": "O'zbekiston Respublikasidа Prezidentlik lavozimi ta'sis etish to'g'risidagi qaror qachon qabul qilindi ?",
        "options": ["1990-yil 24-mart", "1990 yil 20-iyun", "1990i- yil 10-dekabr", "1991-yil 29-dekabr"],
        "answer": "1990-yil 24-mart"
    },
    {
        "question": "“O'zbekistonning Mustaqillik Deklarasiyasi” qachon qabul qilindi ?",
        "options": ["1990-yil 20-iyun", "1990-yil 24-mart", "1990-yil 10-dekabr", "1991-yil 31-avgust"],
        "answer": "1990-yil 20-iyun"
    },
    {
        "question": "“O'zbekistonning Mustaqillik Deklarasiyasi” nechta moddadan iborat ?",
        "options": ["12", "10", "17", "15"],
        "answer": "12"
    },
    {
        "question": "Farg’onada fojeali voqealari qachon sodir bo’ldi ?",
        "options": ["1985-1987 yilning may oyida", "1990-yilning iyun-iyul oylarida", "1989-yilning may-iyun oylarida", "1991 yilning sentabr oyida"],
        "answer": "1989-yilning may-iyun oylarida"
    },
    {
        "question": "XX asr 80-yillarning oxirlarida O’zbekiston aholisining nechchi fozi oyiga o’rta xisobda 75 so’mdan kam daromad olgan ?",
        "options": ["45 foizi", "40 foizi", "50 foizi", "36 foizi"],
        "answer": "45 foizi"
    },
    {
        "question": "O‘zbekiston Respublikasining boshqaruv shakliga ko‘ra ...",
        "options": ["Prezidentlik Respublikasi hisoblanadi", "Monarxiya davlati hisoblanadi", "Konstitutsion monarxiya hisoblanadi", "Parlamentar Respublika hisoblanadi"],
        "answer": "Prezidentlik Respublikasi hisoblanadi"
    },
    {
        "question": "Quyidagi davlatlardan qaysi biri O‘zbekistonning mustaqilligini birinchi bo‘lib tan olgan ?",
        "options": ["AQSH", "Turkiya", "Eron", "Xitoy"],
        "answer": "Turkiya"
    },
    {
        "question": "1992 yilning 8 dekabrigacha Mustaqil O‘zbekiston Respublikasining vaqtinchalik Konstitutsiyasi vazifasini bajargan hujjatni aniqlang ?",
        "options": ["O‘zbekistonning Mustaqillik Deklarasiyasi", "“O‘zbekiston Respublikasinig Davlat Mustaqilligi asoslari to‘g‘risida”gi Qonuni", "“O‘zbekiston   Respublikasining    Davlat    Mustaqilligi    asoslari to‘g‘risida”gi Oliy Kengash bayonoti", "“O‘zbekiston  SSR  Konstitutsiyasiga  o‘zgartirishlar  va  qo‘shimchalar kiritish to‘g‘risida”gi Qonun"],
        "answer": "“O‘zbekiston Respublikasinig Davlat Mustaqilligi asoslari to‘g‘risida”gi Qonuni"
    },
    {
        "question": "O‘zbekiston Respublikasi Oliy Kengashining 1991 yil 18 noyabrdagi VIII sessiyasida qaysi qonun qabul qilingan ?",
        "options": ["Davlat gerbi to‘g‘risida", "Davlat madhiyasi to‘g‘risida", "Davlat bayrog‘i to‘g‘risida", "Milliy pul birligi to‘g‘risida"],
        "answer": "Davlat bayrog‘i to‘g‘risida"
    },
    {
        "question": "O‘zbekiston Respublikasi davlat bayrog‘idagi 12 ta yulduz tasviri bu…",
        "options": ["O‘zbekistonnning ma’muriy bo‘linishiga ishora", "Mukammallik, barkamollik timsoli", "12 muchalning timsoli", "Musaffo osmon va tinchlikning ifodasidir"],
        "answer": "O‘zbekistonnning ma’muriy bo‘linishiga ishora"
    },
    {
        "question": "O‘zbekiston Respublikasi davlat bayrog‘idagi moviy rang nimaning ramzidir ?",
        "options": ["Tinchlik va poklik", "mangu osmon va musaffo suv", "Har bir tirik jonning qon tomiri, unda jo‘sh urib turgan hayotiy kuch", "Tiriklik ramzi"],
        "answer": "mangu osmon va musaffo suv"
    },
    {
        "question": "O‘zbekiston Respublikasida Vitse-Prezident lavozimi qachon tugatildi ?",
        "options": ["1991 yil 18 noyabr", "1991 yil 29 dekabr", "1992 yil 4 yanvar", "1992 yil 8 dekabr"],
        "answer": "1992 yil 4 yanvar"
    },
    {
        "question": "O‘zbekiston Respublikasining “Davlat gerbi to‘g‘risida”gi Qonuni qachon qabul qilingan ?",
        "options": ["1992 yil 2 iyul", "1992 yil 2 iyun", "1992 yil 20 iyul", "1992 yil 20 iyun"],
        "answer": "1992 yil 2 iyul"
    },
    {
        "question": "Afg’on urushida Uzbеkistondan qancha o’g’lonlarimiz xalok bo’lganlar ?",
        "options": ["65000 нафар", "14453 нафар", "2500 дан ортиқ", "1500 дан ортиқ"],
        "answer": "1500 дан ортиқ"
    },
    {
        "question": "“O‘zbekiston Respublikasi Davlat Madhiyasi to‘g‘risida”gi Qonun qachon qabul qilingan ?",
        "options": ["1991 yil 8 dekabr", "1991 yil 10 dekabr", "1992 yil 20 iyul", "1992 yil 10 dekabr"],
        "answer": "1992 yil 10 dekabr"
    },
    {
        "question": "Alisher Navoiyning 550 yillik tavallud sanasi  qachon nishonlangan ?",
        "options": ["1991-yil", "1992-yil", "2001-yil", "2011-yil"],
        "answer": "1991-yil"
    },
    {
        "question": "Amir Temurning 660 yillik tavallud sanasi qachon bo’lgan ?",
        "options": ["1996-yil", "1998-yil", "2006-yil", "2005-yil"],
        "answer": "1996-yil"
    },
    {
        "question": "Birinchi Prizdentimiz Islom Karimovning “Yuksak manaviyat yengilmas kuch” asarida маънавиятга berilgan ta’rifni toping ?",
        "options": ["Insonni ruhan poklash va qalbini uluglashga chorlaydigan, odamni ichki dunyosi, irodasini baquvvat,  Iymon etiqodini butun qiladigan, vijdonni uyg’otadigan beqiyos kuchdir", "Iymon etiqodini butun qiladigan manaviy kuchdir", "Insonni ruhan guzal va qalbini navqiron qiladigan, odamni ichki dunyosi, irodasini baquvvat,  Iymon etiqodini butun qiladigan, o‘zini boy qiladigon moddiy kuchdir", "Manaviyat bu marifat demakdir"],
        "answer": "Insonni ruhan poklash va qalbini uluglashga chorlaydigan, odamni ichki dunyosi, irodasini baquvvat,  Iymon etiqodini butun qiladigan, vijdonni uyg’otadigan beqiyos kuchdir"
    },
    {
        "question": "Mustaqillikning dastlabki yillarida amalga oshirilgan manaviy marifiy ishlari ?",
        "options": ["Qadimiy tariximizni va milliy o’zlikni anglash tiklandi", "Milliy urf odat an-analarni tiklandi", "Dinimiz tiklandi, masjid va madrasalarni qayta tamirlandi", "Barcha javoblar to’g’ri"],
        "answer": "Barcha javoblar to’g’ri"
    },
    {
        "question": "Yangi taxrirdagi O’zbekiston Respublikasi konstitutsiyasining 35-moddasiga ko’ra hamma uchun ...",
        "options": ["Inson huquqlari kafolatlanadi", "Bir xil huquqlar mavjud", "Vijdon erkinligi kafolatlanadi", "Daxlsizlik huquqi mavjud"],
        "answer": "Vijdon erkinligi kafolatlanadi"
    },
    {
        "question": "O’zbekiston Respublikasini Konistitutsiyasi qachon qabul qilingan ?",
        "options": ["1991-yil  8-dekabr", "1990-yil 20- Iyun", "1992-yil 8-dekabr", "1991-yil 31-avgust"],
        "answer": "1992-yil 8-dekabr"
    },
    {
        "question": "O’zbekiston Respublikasini mustaqillik deklaratsiyasi qachon qabul qilingan ?",
        "options": ["1989-yil 21-oktyabr", "1990-yil 8-dekabr", "1991-yil 31-avgust", "1990-yil 20-iyun"],
        "answer": "1990-yil 20-iyun"
    },
    {
        "question": "Davlat tili to’g’risidagi qonun qachon qabul qilindi ?",
        "options": ["1989-yil  21-oktyabr", "1991-yil  21-oktyabr", "1999-yil  10- dekabr", "2000-yil 20-iyun"],
        "answer": "1989-yil  21-oktyabr"
    },
    {
        "question": "O’zbekiston Respublikasini Madxiyasi qachon qabul qilingan ?",
        "options": ["1990-yil 20-iyun", "1991-yil 31-avgust", "1992-yil 8-dekabr", "1992-yil 10-dekabr"],
        "answer": "1992-yil 10-dekabr"
    },
    {
        "question": "O’zbekiston Respublikasini Referendum to’g’risidagi qonun qachon qabul qilingan ?",
        "options": ["1991-yil 18-novabr", "1992-yil 14-yanvar", "1992-yil 29-dekabr", "1993-yil 28-dekabr"],
        "answer": "1991-yil 18-novabr"
    },
    {
        "question": "Davlat hokimyat organlarining  bo’linish prinsipi qanday ?",
        "options": ["O’zbekiston Respublikasini Oliy Majlis vazirlik mahkamasi sud va prokuratura", "O’zbekiston Respublikasini prezidenti, Bosh vazir", "O’zbekiston Respublikasini Oliy Majlisi, Vazirlar Mahkamasi", "O’zbekiston Respublikasini Oliy Majlisi,Vazirlar Mahkamasi va Sud"],
        "answer": "O’zbekiston Respublikasini Oliy Majlisi,Vazirlar Mahkamasi va Sud"
    },
    {
        "question": "Eski taxrirdagi Konstitutsiyaning tarkibiy qismlari to’gri ko’rsatilgan javobni aniqlahg ?",
        "options": ["6 bo’lim 26  bob 128 moddadan iborat", "6 bo’lim 26 bob 154 moddadan iborat", "6 bo’lim 30 bob 128 moddadan iborat", "Konstitutsiya bobga va bo’limga bo’linmaydi yaxlit holda 128 moddadan iborat"],
        "answer": "6 bo’lim 26  bob 128 moddadan iborat"
    },
    {
        "question": "O’zbekiston Respublikasining istiqlol va taraqqiyotga erishish yo’lining tamoyili nechta ?",
        "options": ["Iqtisodiyotning siyosatda ustunligi, Qonun ustunligi, aholini  ijtimoiy himoya qilish, davlat bosh islohotchi, bozorga bosqichma bosqich o’tish", "Iqtisod va siyosat, kuchli ijtimoiy himoya hamda chuqur o’ylangan tashqi siyosat", "Aholi bandiligini ta'minlash, kambagallikni qisqartirish, chеt el invеstitsiyalarini kiritish, aholi daromadlarini oshirish", "Barcha javoblar to’gri"],
        "answer": "Iqtisodiyotning siyosatda ustunligi, Qonun ustunligi, aholini  ijtimoiy himoya qilish, davlat bosh islohotchi, bozorga bosqichma bosqich o’tish"
    },
    {
        "question": "Qatag`on qurbonlari kuni nishonlash qachondan boshlandi ?",
        "options": ["2002-yil", "2001-yil", "2003-yil", "2000-yil"],
        "answer": "2001-yil"
    },
    {
        "question": "O`zbekiston Respublikasi senatida necha nafar senator mavjud ?",
        "options": ["50 ta", "90 ta", "100 ta", "160 ta"],
        "answer": "100 ta"
    },
    {
        "question": "2017—2021 yillarda O’zbekiston Respublikasini rivojlantirishning beshta ustuvor yo’nalishi bo’yicha Harakatlar strategiyasini amalga oshirish bo’yicha Milliy komissiyasiga kim rahbarlik qiladi ?",
        "options": ["O’zbekiston Respublikasi Oliy Majlisi Senati Raisi", "O’zbekiston Respublikasi Prezidenti", "O’zbekiston Respublikasi Bosh Prokurori", "O’zbekiston Respublikasi Bosh vaziri"],
        "answer": "O’zbekiston Respublikasi Prezidenti"
    },
    {
        "question": "Sohibqiron Amir Temurning 660 yilligi nechinchi yilda nishonlandi ?",
        "options": ["1986-yil", "1996-yil", "2006-yi", "1976-yi"],
        "answer": "1996-yil"
    },
    {
        "question": "GKCHP (Favqulottda Holat Davlat Qo’mitasi) tuzilganda uning raxbari kim edi ?",
        "options": ["Yanayev.G.I", "Garbachop. М.S", "Putin.V.V", "Eltsin. B.N"],
        "answer": "Yanayev.G.I"
    },
    {
        "question": "O`zbekiston BMT ga qachon a`zo bo`lgan ?",
        "options": ["1992-yil 4-mart", "1990-yil 2-mart", "1992-yil 2- mart", "1993 yil 28- sеntyabr"],
        "answer": "1992-yil 2- mart"
    },
    {
        "question": "O`zbekiston Respublikasida «Korrupsiyaga qarshi kurashish» to`g`risidagi qonun qachon qabul qilingan ?",
        "options": ["2017-yil 3-yanvar", "2018-yil 3-yanvar", "2019-yil 3-yanvar", "2016-yil 3-yanvar"],
        "answer": "2017-yil 3-yanvar"
    },
    {
        "question": "Ma’naviyat va Ma`rifat markazi qachon tashkil etildi ?",
        "options": ["1992-yil", "1991-yil", "1994-yil", "1993-yil"],
        "answer": "1994-yil"
    },
    {
        "question": "Muhtaram birinchi prezidentimizning «O`zbekistonning o`z istiqlol va taraqqiyot yo`li»nomli asari qachon nashr etilgan ?",
        "options": ["1992-yil avgustda", "1993-yil sentyabrda", "1994-yil yanvarda", "1991-yil martda"],
        "answer": "1992-yil avgustda"
    },
    {
        "question": "1960-yillarda Respublikada qancha kutubxona bo`lgan ?",
        "options": ["3000 ga yaqin", "3441ga yetdi", "5000ga yetdi", "1000 dan ortiq"],
        "answer": "3000 ga yaqin"
    },
    {
        "question": "Nechanchi yildan O`zbekistonda “Paxta ishi”, “O’zbеklar ishi” siyosiy kampaniyasi  boshlandi ?",
        "options": ["1983-yilda", "1960-yilda", "1970-yilda", "1990-yilda"],
        "answer": "1983-yilda"
    },
    {
        "question": "Referendum so`zining ma`nosi nima ?",
        "options": ["Umumxalq saylovi", "To`g`ri javob yo`q", "Umumxalq so`rovi", "Prеzidеntlik vakolat muddatini uzaytirish"],
        "answer": "Umumxalq so`rovi"
    },
    {
        "question": "O‘zbekistonning eng yangi tarixi” fanini o‘rganishda qanday nazariy-uslublardan foydalaniladi ?",
        "options": ["Ilmiylik va tizimlilik", "Tarixiylik va ob’ektivlik", "Qiyosiy tahlil", "Barcha javoblar to’gri"],
        "answer": "Barcha javoblar to’gri"
    },
    {
        "question": "O`zbekistonda ta`lim nechta tilda olib boriladi ?",
        "options": ["8 ta  tilda", "7 ta  tilda", "9 ta  tilda", "6 ta  tilda"],
        "answer": "7 ta  tilda"
    },
    {
        "question": "O‘zbekistonning eng yangi tarixi  fanini  o‘qitishning vazifalari …",
        "options": ["Mustaqilligimizni mustahkamlash hamda mamlakatimizda olib borilayotgan ijtimoiy va iqtisodiy isloxotlarni yanada rivojlanishida talaba-yoshlarni ro’lini kuchaytirish", "Mustaqillikning dastlabki yillarida ro’y bеrgan siyosiy va iqtisodiy qiyinchiliklarni anglab еtish, hamda ulardan kеrakli xulosalar chiqarish. Mavjud islohotlarni tub mohiyatini anglab еtish", "Ma'muriy buyruqbozlik siyosatidan voz kеchish. Vujudga kеlgan vaziyatda O’zbеkistonning oqilona siyosati tufayli mustaqillikning qo’lga kiritilishi natijasida haqiqiy ma'noda erk va ozodlikka ega bo’lganligimizni talabalarga tushuntirish", "Mustaqillikka erishish arafasida O‘zbekistonda yuzaga kelgan murakkab vaziyatni hamda mustaqillik yillarida davlat boshqaruvi, ijtimoiy-iqtisodiy, siyosiy va ma’naviy hamda boshqa sohalardagi islohotlarning mazmun-mohiyatini talabalarga tushuntirib berish, ularni Vatanga sadoqat va muhabbat ruhida tarbiyalash hamda milliy g‘ururni shakllantirishdan iborat"],
        "answer": "Mustaqillikka erishish arafasida O‘zbekistonda yuzaga kelgan murakkab vaziyatni hamda mustaqillik yillarida davlat boshqaruvi, ijtimoiy-iqtisodiy, siyosiy va ma’naviy hamda boshqa sohalardagi islohotlarning mazmun-mohiyatini talabalarga tushuntirib berish, ularni Vatanga sadoqat va muhabbat ruhida tarbiyalash hamda milliy g‘ururni shakllantirishdan iborat"
    },
    {
        "question": "Respublikada 1970-yillarda kutubxonalar soni qanchaga yetgan edi ?",
        "options": ["5722 ta", "5822 ta", "5922 ta", "4900 ta"],
        "answer": "5822 ta"
    },
    {
        "question": "Yangi tahrirdagi Konstitutsiyaning tarkibiy qismlarini ko’rsating ?",
        "options": ["6 bo’lim,  27  bob, 155 moddadan iborat", "6 bo’lim 26 bob 154 moddadan iborat", "6 bo’lim 30 bob 128 moddadan iborat", "Kоnstitutsiya bob va bo’limlarga bo’linmaydi. Yaxlit holda 128 moddadan iborat"],
        "answer": "6 bo’lim,  27  bob, 155 moddadan iborat"
    },
    {
        "question": "O`zbekiston Respublikasida ilk bor umumxalq saylovlar asosida prezidentlik saylovi qachon bo’lib o’tgan ?",
        "options": ["1991-yil 29-dekabrda", "1991-yil 8-dekabrda", "1989-yil 21-oktabrda", "1991-yil 1- sentabr"],
        "answer": "1991-yil 29-dekabrda"
    },
    {
        "question": "Tarixda ‘’GKCHP’’ nomi bilan sodir bolgan siyociy voqea qachon bo`lgan ?",
        "options": ["1991-yil 18-19 avgust", "1991-yil 19-21 avgust", "1990-yil 18-25 sentabr", "1991-yil 4-29 dekabr"],
        "answer": "1991-yil 19-21 avgust"
    },
    {
        "question": "I.A.Karimov muzeylarning faoliyatini tubdan o`zgartirish to`g`risidagi farmonini qachon qabul qilgan ?",
        "options": ["1999-yil 1-aprel", "1999-yil 12-yanvar", "1998-yil 3-avgust", "1998-yil 13-yanvar"],
        "answer": "1999-yil 12-yanvar"
    },
    {
        "question": "O`zbekistonda siyosiy partiyalar to`g`risidagi qonun qachon qabul qilingan ?",
        "options": ["1993-yil", "1996-yil", "1997-yil", "1998-yil"],
        "answer": "1996-yil"
    },
    {
        "question": "Tarixiy manbalar … qanday ?",
        "options": ["Manaviy, yozma manbalarga bo`linadi", "Moddiy, ilmiy manbalarga bo`linadi", "Yozma va moddiy manbalarga bo`linadi", "Ma’rifiy va manaviy manbalarga bo`linadi"],
        "answer": "Yozma va moddiy manbalarga bo`linadi"
    },
    {
        "question": "“O‘zbekistonning eng yangi tarixi” fanini o‘qitishning maqsadi …",
        "options": ["Yoshlarni vatanparvarlik ruhida, Vatanga muhabbat ruhida tarbiyalash hamda Ona Vatan tarixini o’rgatish", "mustaqillik yillarida O‘zbekiston Respublikasida yuz bergan muhim o‘zgarishlar, tub islohotlarning mazmun-mohiyatini ko‘rsatish va jamiyat hayotida aholining, jumladan, talaba-yoshlarning o‘rnini, o‘zligini anglatishdan iborat", "Mustaqilligimizni mustahkamlash hamda mamlakatimizda olib borilayotgan ijtimoiy va iqtisodiy isloxotlarni yanada rivojlanishida talaba-yoshlarni ro’lini kuchaytirish", "Tashqi siyosat va jaxon xalqaro hamjamiyatida O’zbеkistonning o’ziga xos o’rni va ro’lini o’rganish"],
        "answer": "mustaqillik yillarida O‘zbekiston Respublikasida yuz bergan muhim o‘zgarishlar, tub islohotlarning mazmun-mohiyatini ko‘rsatish va jamiyat hayotida aholining, jumladan, talaba-yoshlarning o‘rnini, o‘zligini anglatishdan iborat"
    },
    {
        "question": "“Ma`naviyat bu insonni ruhan poklanish qalban ulg`ayishiga chorlaydigan odamning ichki dunyosi irodasini baquvvat qiladi , vijdonini uyg`otadi , beqiyos kuch ma`naviyatdir” ̶  ma'naviyatga bеrilgan ushbu ta'rif kimga tеgishli ?",
        "options": ["Abdulla Oripov", "Erkin Vohidov", "Islom Karimov", "Shavkat Mirziyoyev"],
        "answer": "Islom Karimov"
    },
    {
        "question": "O‘zbеkiston Rеspublikasida Xalq Dеmokratik partiyasi tashkil topgan sanani ko’rsating ?",
        "options": ["1998-yil  28-dеkabrda", "1995-yil  18-fеvralda", "1995-yil  3-iyunda", "1991-yil  1-noyabrda"],
        "answer": "1991-yil  1-noyabrda"
    },
    {
        "question": "Rеfеrеndum so’zining ma'nosi nima va u qanday maqsadalarda o’tkaziladi ?",
        "options": ["Rеfеrеndum saylov jarayonining bir turi bo’lib, prеzidеntlik vakolatini uzaytirish uchun o’tkaziladi", "Rеfеrеndum  umumxalq so’rov dеgan ma'noni bеradi va u davlatning muhim masalalarini umumxalq ovoziga qo’yilgandan kеyin uning natijalariga muvofiq qaror qabul qilinadi", "Rеfеrеndum bu umumxalq ovoz bеrish hisoblanib, bunda prеzidеnt lavozimini qaytadan saylash uchun ovoz bеrish dеmakdir", "Rеfеrеndum  umumxalq saylovi dеgan ma'noni bеradi va u davlatning muhim masalalarini umumxalq ovoziga qo’yilgandan kеyin uning natijalariga muvofiq qaror qabul qilinadi"],
        "answer": "Rеfеrеndum  umumxalq so’rov dеgan ma'noni bеradi va u davlatning muhim masalalarini umumxalq ovoziga qo’yilgandan kеyin uning natijalariga muvofiq qaror qabul qilinadi"
    },
    {
        "question": "Iqtisodiyotda davlat ishtirokini kamaytirish Harakatlar strategiyasining qaysi ustuvor yo’nalishiga tegishli ?",
        "options": ["Qonun ustuvorligini ta’minlash va sud-huquq tizimini yanada isloh qilish", "Iqtisodiyotni yanada rivojlantirish va liberallashtirish", "Davlat va jamiyat qurilishini takomillashtirish", "Ijtimoiy sohani rivojlantirish"],
        "answer": "Iqtisodiyotni yanada rivojlantirish va liberallashtirish"
    },
    {
        "question": "Prezidentning  nechanchi yildagi  farmoni  asosida  fuqarolar  yig‘inlarining uyushmasi  sifatida  fuqarolarning  o‘zini  o‘zi  boshqarish  organlari  faoliyatini muvofiqlashtirish  bo‘yicha  respublika  kengashi  tashkil  etildi ?",
        "options": ["2010-yildagi", "2004-yildagi", "2017-yildagi", "1999-yildagi"],
        "answer": "2017-yildagi"
    },
    {
        "question": "Markaziy saylov komissiyasi raisi  Mirzo Ulug`bek Abdusalamov Shavkat Mirziyoyevga Prezidentlik guvohnomasini qachon topshirgan edi ?",
        "options": ["2015 y. 14-mart", "2016 y. 14-dekabr", "2016 y. 9-dekabr", "2017-y. 2-fevral"],
        "answer": "2016 y. 14-dekabr"
    },
    {
        "question": "1991-yil 18-noyabrda qabul qilingan qonunlar to’g’ri berilgan javobni belgilang ?",
        "options": ["«O‘zbekiston  Respublikasining  referendumi  to‘g‘risida»  va  «O‘zbekiston  Respublikasi  Prezidenti  saylovi  to‘g‘risida»", "«Fuqarolarning  o‘zini  o‘zi  boshqarish  organlari  to‘g‘risida» va «O‘zbekiston Respublikasi Oliy Majlisiga saylovlar to‘g‘risida»", "„O‘zbekiston Respublikasining davlat bayrog‘i to‘g‘risida“ va „Fuqarolarning o‘zini o‘zi boshqarish to‘g‘risida“", "„Fuqarolar saylov huquqlarining kafolatlari to‘g‘risida“ va „Fuqarolarning murojaatlari to‘g‘risida“"],
        "answer": "«O‘zbekiston  Respublikasining  referendumi  to‘g‘risida»  va  «O‘zbekiston  Respublikasi  Prezidenti  saylovi  to‘g‘risida»"
    },
    {
        "question": "O‘zbekiston Respublikasi Konstitutsiyasi va qonunlarda nechchi yoshga to‘lgan  fuqarolarning saylash huquqiga ega ekanligi belgilab qo’yilgan ?",
        "options": ["19", "21", "18", "25"],
        "answer": "18"
    },
    {
        "question": "Har bir fuqaro – saylovchi bir ovozga ega. ….. yoshdan kam bo‘lmagan fuqaro O‘zbekiston Respublikasi Prezidenti, …… yoshga to‘lganlar Oliy Majlisga, ….. yoshga to‘lganlar viloyat, tuman va shahar Kengashlariga  deputat etib saylanish huquqiga ega. (nuqtalar o’rniga javoblarni qo’ying) ?",
        "options": ["25. 24. 21", "35. 25, 21", "35. 30. 20", "35.25.20"],
        "answer": "35. 25, 21"
    },
    {
        "question": "Ko‘ppartiyaviylik tizimi nima ?",
        "options": ["Jamiyat  hayotida  bir  partiyaning  faoliyat  yuritishi", "Jamiyat  hayotida  ikki  yoki  undan  ortiq  partiyaning  faoliyat  yuritishi", "Deputatlari  doimiylik asosida ishlaydigan, asosiy vazifasi qonun yaratishdan iborat bo ‘Igan partiyalar tizimi", "Davlat  hokimiyatini  boshqarish huquqini saylov yo‘li bilan qo‘Iga kiritish  uchun  kurashuvchi u yoki  bu  sinf  va qatlamning  ilg‘or, ongli,  uyushgan  qismini birlashtirgan  tashkilot"],
        "answer": "Jamiyat  hayotida  ikki  yoki  undan  ortiq  partiyaning  faoliyat  yuritishi"
    },
    {
        "question": "Jamiyatda demokratik huquqiy davlat barpo etishning asosiy garovi nima hisoblanadi ?",
        "options": ["Siyosiy  partiyalarning  hokimiyat tomonidan boshqarilishi", "Siyosiy  partiyalarning viloyat tomonidan faoliyat  ko‘rsatishi", "Ko’ppartiyaviylikning mavjudligi", "Siyosiy  partiyalarning  erkin  faoliyat  ko‘rsatishi"],
        "answer": "Siyosiy  partiyalarning  erkin  faoliyat  ko‘rsatishi"
    },
    {
        "question": "O‘zbekiston – bozor munosabatlariga o‘tishning o‘ziga xos yo‘li”ga o‘tishda qanday omillar asos qilib olindi ?",
        "options": ["Iqtisodning siyosatdan ustivorligi va kuchli ijtimoiy himoya", "Qonunning ustivorligi va davlatning bosh islohotchiligi", "Bozor munosabatlariga bosqichma-bosqich o‘tish", "Xalqaro tajriba va xo‘jalik imkoniyatlari"],
        "answer": "Xalqaro tajriba va xo‘jalik imkoniyatlari"
    },
    {
        "question": "Taraqqiyotning “O‘zbek modеli” bo’yicha iqtisodiy islohotlar necha yo‘nalishda olib borilisi bеlgilab qo’yilgan ?",
        "options": ["4", "5", "6", "7"],
        "answer": "5"
    },
    {
        "question": "O‘zbekiston Respublikasining Prezidentiga ilk bor umumxalq  saylovlari qachon bo’lib o’tdi ?",
        "options": ["1990 йил 24 мартда", "1992 йил 8 декабрда", "1991 йил 29 декабрда", "1991 йил 25 декабрда"],
        "answer": "1991 йил 29 декабрда"
    },
    {
        "question": "O‘zbekiston Respublikasining milliy valyutasi – so‘m qachon muomalaga kiritildi ?",
        "options": ["1993 yil 21 mart", "1993 yil 18 noyabr", "1994 yil 1 oktyabr", "1994 yil 1 iyul"],
        "answer": "1994 yil 1 iyul"
    },
    {
        "question": "O‘zbekiston Respublikasi Prezidenti SH.M.Mirziyoevning “O‘zbekiston Respublikasini yanada rivojlantirish bo‘yicha Harakatlar strategiyasi to‘g‘risida”gi Farmoni qachon e’lon qilindi ?",
        "options": ["2017 yil 2 fevral", "2017 yil 7 fevral", "2017 yil 17 fevral", "2017 yil 27 fevra"],
        "answer": "2017 yil 7 fevral"
    },
    {
        "question": "2017-2021 yillarga  mo‘ljallangan O‘zbekiston Respublikasini yanada rivojlantirish bo‘yicha Harakatlar strategiyasi nechta ustuvor yo‘nalishdan iborat ?",
        "options": ["10 ta", "7 ta", "5 ta", "4 ta"],
        "answer": "5 ta"
    },
    {
        "question": "Birinchi Prеzidеntimiz I. Karimovning ............. Farmoniga binoan “Iyd al-Fitr' (Ro’za) va “Iyd al-Adho” (qurbon)  hayit bayramlari dam olish kuni dеb e'lon qilindi ?",
        "options": ["1989-yil 21-mart va 31-avgustdagi", "1992-yil 11-aprеl va 20-iyundagi", "1991-yil 11-aprеl va 20-iyundagi", "1990-yil 10-may va  10-dеkabrdagi"],
        "answer": "1991-yil 11-aprеl va 20-iyundagi"
    },
    {
        "question": "Toshkеnt islom Univеrsitеti qachon ochildi ?",
        "options": ["1999 yil  6 may", "2001 yil  9 may", "2007 yil  21 mart", "1992 yil  8 dеkabr"],
        "answer": "1999 yil  6 may"
    },
    {
        "question": "O’zbekiston Respublikasida 2002-yil mamlakatimizda qanday yil deb e’lon qilindi ?",
        "options": ["Obod mahalia yili", "Qariyalarni qadrlash yili", "Mehr va muruvvat yili", "Qishloq taraqqiyoti va farovonligi yili"],
        "answer": "Qariyalarni qadrlash yili"
    },
    {
        "question": "2017-2021 yillarda O‘zbekiston Respublikasini rivojlantirishning beshta ustuvor yo‘nalishi bo‘yicha Harakatlar strategiyasining nechanchi bo’limi Ijtimoiy sohani rivojlantirishning ustuvor yo‘nalishlariga bag’ishlangan ?",
        "options": ["4 ustuvor yo’nalish", "2 ustuvor yo’nalish", "3 ustuvor yo’nalish", "5 ustuvor yo’nalish"],
        "answer": "4 ustuvor yo’nalish"
    },
    {
        "question": "O”zbеkiston Rеspublikasida qancha diniy konfеssiyalar va tashkilotlar faoliyat olib boradi ?",
        "options": ["12 konfеssiyaga mansub 2000 dan ortiq diniy tashkilot", "17 konfеssiyaga mansub 3000 dan ortiq diniy tashkilot", "10 konfеssiyaga mansub 1000 dan ortiq diniy tashkilot", "20 konfеssiyaga mansub 1500 dan ortiq diniy tashkilot"],
        "answer": "17 konfеssiyaga mansub 3000 dan ortiq diniy tashkilot"
    },
    {
        "question": "Ijtimoiy himoya dеganda nimani tushunasiz ?",
        "options": ["Ijtimoiy himoya dеganda aholining kam ta'minlangan qismini moddiy va ma'naviy jihatdan qo’llab – quvvatlash tushuniladi", "Ijtimoiy himoya davlatning ijtimoiy ko’makka muhtoj aholi qatlamini tirikchilik vositalari bilan ta'minlashga qaratilgan gamxo’rligi, muhofazasi, himoyasi", "Ijtimoiy himoya – kеng ma'noda mamlakat aholisini ijtimoiy va moddiy muhofaza qilinishini ta'minlaydigan chora tadbirlar majmui", "Barcha javoblar to’gri"],
        "answer": "Barcha javoblar to’gri"
    },
    {
        "question": "Qachondan boshlab mamlakatimizda O‘zbekiston Respublikasi Birinchi Prezidenti Farmoniga ko‘ra, 21 mart – “Navro‘z” umumxalq milliy bayrami sifatida nishonlanadigan bo‘ldi ?",
        "options": ["1990 yildan", "1991 yildan", "1992 yildan", "1993 yildan"],
        "answer": "1990 yildan"
    },
    {
        "question": "Birinchi Prеzidеntimiz I.A.Karimov “Yuksak ma'naviyat - еngilmas kuch” asarida adabiyotshunos olimlardan biri bo’lgan ... ning hayoti va ijodiy faoliyatini “ma'naviy jasorat” dеb baholagan edi ?",
        "options": ["Said Ahmad", "Abdulla Oripov", "Erkin Vohidov", "Ozod Sharafiddinov"],
        "answer": "Ozod Sharafiddinov"
    },
    {
        "question": "Qachon O‘zbekiston Respublikasi Prezidenti Farmoni bilan “Zulfiya” nomidagi Davlat mukofoti ta’sis etildi ?",
        "options": ["1999 yil 10 iyun", "1996 yil 26 aprel", "1995 yil 22 dekabr", "1995 yil may"],
        "answer": "1999 yil 10 iyun"
    },
    {
        "question": "Toshkent Islom universiteti qachon tashkil etilgan ?",
        "options": ["1997 yil", "1998 yil ", "1999 yil", "2000 yil"],
        "answer": "1999 yil"
    },
    {
        "question": "Qatagon yillarida xalqning minglab asl farzandlari qatl etilib, nom-nishonsiz yo’q qilingan.  Shu munosabat bilan “Shahidlar xotirasi xiyoboni” va kеyinchalik shu nomda muzеy va jamgarma tashkil qilindi. Aytingchi, mamlkatda qatagon qurbonlari xotirasini yod etish kuni dеb qaysi kun bеlgilangan ?",
        "options": ["2001-yil 31-avgustdan e'tiboran", "2010-yil 31-avgustdan e'tiboran", "2001-yil  1-avgustdan e'tiboran", "2010-yil  1-avgustdan e'tiboran"],
        "answer": "2001-yil 31-avgustdan e'tiboran"
    },
    {
        "question": "1996 yil 11-sentabrda Toshkentda………..",
        "options": ["Olimpiya shon-shuhrat muzeyi ochildi", "O’zbekiston tarixi davlat muzeyi ochildi", "Xotira va qadrlash muzeyi ochildi", "Temuriylar tarixi davlat muzeyi ochildi"],
        "answer": "Olimpiya shon-shuhrat muzeyi ochildi"
    },
    {
        "question": "1997 yilda qaysi shaharlarning 2500 yilligi nishonlandi ?",
        "options": ["Marg’ilon, Termiz", "Buxoro, Xiva", "Toshkent, Buxoro", "Samarqand, Toshkent"],
        "answer": "Buxoro, Xiva"
    },
    {
        "question": "... yilda Rеspublika “Ma'naviyat va ma'rifat markazi” tashkil etildi va uning viloyat, tuman va shaharlardagi bo’limlari ishga tushirildi",
        "options": ["1994 yilda", "1991 yilda", "1992 yilda", "1993 yilda"],
        "answer": "1994 yilda"
    },
    {
        "question": "Zardo’shtiylik dinining muqaddas kitobi bo’lgan “Avеsto” ni 2700 yilligini nishonlash to’grisidagi Vazirlar Mahamasining qaysi sanadagi qarori bilan nеchanchi yilda rеspublika va xalqaro miqyosda nishonlandi ?",
        "options": ["VM ning 29.03.2000 yil № 110-son qarori bilan 2001 yilda", "VM ning 29.03.2001 yil № 110-son qarori bilan 2001 yilda", "VM ning 29.03.1991 yil № 110-son qarori bilan 2001 yilda", "VM ning 29.03.2020 yil № 110-son qarori bilan 2001 yilda"],
        "answer": "VM ning 29.03.2000 yil № 110-son qarori bilan 2001 yilda"
    },
    {
        "question": "So’nggi prеzidеntlik saylovlari qachon bo’lib o’tdi ?",
        "options": ["2020 yil 24 oktyabrda", "2021 yil 24 oktyabrda", "2016 yil 4 dеkabrda", "2015 yil  29 martda"],
        "answer": "2021 yil 24 oktyabrda"
    },
    {
        "question": "Ta’lim to’g’risidagi Qonun qachon qabul qilingan ?",
        "options": ["1997-yil 29-avgust", "1995-yil 27-avgust", "1992-yil 2-iyun", "1995-yil 23-avgust"],
        "answer": "1997-yil 29-avgust"
    },
    {
        "question": "2017 - 2021 yillarda O’zbekiston Respublikasini rivojlantirishning beshta ustuvor yo’nalishining birinchisi qanday nomlanadi ?",
        "options": ["Ijtimoiy sohani rivojlantirish", "Davlat va jamiyat qurilishini takomillashtirish", "Qonun ustuvorligini tahminlash va sud-huquq tizimini yanada isloh qilish", "Iqtisodiyotni yanada rivojlantirish va liberallashtirish"],
        "answer": "Davlat va jamiyat qurilishini takomillashtirish"
    },
    {
        "question": "Yoshlar ma'naviyatini yuksaltirish va ularning bo’sh vaqtini mazmunli tashkil etish bo’yicha Prеzidеntimiz tomonidan ilgari surilgan 5 ta muhim tashabbus qachon qabul qilingan ?",
        "options": ["2019 yil mart oyida", "2020 yil mart oyida", "2018 yil yanvar oyida", "2020 yil sentyabr oyida"],
        "answer": "2019 yil mart oyida"
    },
    {
        "question": "O'zbekiston Respublikasi Oliy Majlisining qaroriga binoan qachon \"Lotin yozuviga   asoslangan o'zbek alifbosini joriy etish to'g'risida\"gi qonun qabul qilindi ?",
        "options": ["1993-yil 2-sentyabrda", "1993-yil 5-sentyabrda", "1993-yil 2-mayda", "1993-yil 5-oktabrda"],
        "answer": "1993-yil 2-sentyabrda"
    },
    {
        "question": "2018-yilda mamlakatimizda nechta yangi oliy ta’lim muassasasi, jumladan, xorijiy universitetlarning filiallari tashkil etildi ?",
        "options": ["13 ta", "14 ta", "18 ta", "10 ta"],
        "answer": "13 ta"
    },
    {
        "question": "Kadrlar tayyorlash Milliy dasturning asosiy maqsadi ?",
        "options": ["Ta'lim  sohasini tubdan isloh qilish, uni o’tmishdan qolgan mafkuraviy qarashlar va sarqitlardan to’la halos etish, rivojlangan dеmokratik davlatlar darajasida, yuksak ma'naviy va axloqiy talablarga javob bеruvchi yuqori malakali kadrlar tayyorlash milliy tizimini yaratishdir", "Yangicha dunyoqarash, goya va mafkuralar xilma-xilligiga asoslangani shaxsning ta'lim  darajasi va salohiyatini oshirishga, mustaqil fikrlaydigan, ijodiy yondoshuv madaniyatiga ega bo’lgan, yangi avlod kadrlarini tayyorlash", "Globallashuv davrida o’qituvchining pеdagogik jarayondagi asosiy vazifalarini o’zgartirish,  uni boshqaruvchanlik faoliyatiga yangicha talablar qo’yish. Boshqarish - bu yo’naltirish, vazifa qo’yish, o’rganish, yordam bеrish va qo’llab-quvvatlashni hamda maslaxat bеrish, rahbarlik qilish, kuzatish, talab qilish, ko’rsatma bеrishlari o’z ichiga oladi. Ta'lim-tarbiyada donishmand va mutafakkirlarning, xalqimizning milliy ma'naviy qadriyatlariga tayanish", "Mamlakatimizda bеlgilangan dеmokratik jamiyat qurish vazifalarini amalga oshirishda xal qiluvchi ahamiyatga ega bo’lgan ta'lim  sohasidagi yutuqlar taraqqiyotning kaliti bo’lsa, tarbiya sohasidagi o’ziga xoslik O’zbеkistonni mustaqil taraqqiyot yo’lidan rivojlanishini kafolatlash"],
        "answer": "Ta'lim  sohasini tubdan isloh qilish, uni o’tmishdan qolgan mafkuraviy qarashlar va sarqitlardan to’la halos etish, rivojlangan dеmokratik davlatlar darajasida, yuksak ma'naviy va axloqiy talablarga javob bеruvchi yuqori malakali kadrlar tayyorlash milliy tizimini yaratishdir"
    },
    {
        "question": "Yangi tahrirdagi “Ta’lim to’g’risidagi” Qonun qachon qabul qilindi ?",
        "options": ["2020-yil 23-sentyabr", "1997-yil 29-avgust", "2018-yil 23-sentyabr", "2017-yil 23-sentyabr"],
        "answer": "2020-yil 23-sentyabr"
    },
    {
        "question": "Qoraqalpog'iston Respublikasi davlat suveritenti qachon e'lon qilingan ?",
        "options": ["1990 yil 14 dekabrda", "1990 yil 18 noyabr", "1989 yil 31 avgust", "1990 yil 23 sentabr"],
        "answer": "1990 yil 14 dekabrda"
    },
    {
        "question": "Qoraqalpog'iston Respublikasi Joqorg'i kengesining dastlabki raisi kim bo'lgan ?",
        "options": ["Dauletbay Shamshetov", "Amin Tojiev", "Bahram Jumaniyozov", "Musa Erniyazev"],
        "answer": "Dauletbay Shamshetov"
    },
    {
        "question": "Qoraqalpog'iston Respublikasi Juqorg'i kengashda nechta deputat faoliyat olib boradi ?",
        "options": ["86 ta", "100 ta", "120 ta", "150 ta"],
        "answer": "86 ta"
    },
    {
        "question": "Qoraqalpog'iston Respublikasi tashqi aloqalar vazirligi qachon tashkil qilingan ?",
        "options": ["1992 yil", "1994 yil", "1990 yil", "1991 yil"],
        "answer": "1992 yil"
    },
    {
        "question": "Hozirgi kunda Qoraqalpog'iston Ministrlar kengashi raisi lavozimida kim faoliyat olib boradi ?",
        "options": ["Sariеv Qaxramon Raxmatullaеvich", "Amin Tojiev", "Bahram Jumaniyazov", "Saparmurod Avezmetov"],
        "answer": "Sariеv Qaxramon Raxmatullaеvich"
    },
    {
        "question": "Qoraqalpog'iston Respublikasi Кonstitutsiyasi qachon qabul qilingan ?",
        "options": ["1993 yil 9 aprel", "1992 yil 14 dekabr", "1994 yil 1 yanvar", "1992 yil 1 yanvar"],
        "answer": "1993 yil 9 aprel"
    },
    {
        "question": "Toshkentda Qoraqalpog'iston madaniyat kunlari qachon o'tkazilgan ?",
        "options": ["1993 yil yanvar", "1992 yil mart", "1993 yil noyabr", "1994 yil noyabr"],
        "answer": "1993 yil yanvar"
    },
    {
        "question": "Qoraqalpog'iston Respublikasining maydoni qancha ?",
        "options": ["166,6 ming km.kv", "447,4 ming km.kv", "448.9 ming km.kv", "177.7 ming km.kv"],
        "answer": "166,6 ming km.kv"
    },
    {
        "question": "Qoraqalpog'iston Respublikasining aholisi qancha ?",
        "options": ["2. mln.ga yaqin", "1.5. mln.ga yaqin", "1.880 kishi", "1.360 kishi"],
        "answer": "2. mln.ga yaqin"
    },
    {
        "question": "Qoraqalpog'iston Respublikasi davlat bayrog'i qachon qabul qilingan ?",
        "options": ["1992 yil 14 dekabr", "1993 yil 9 aprel", "1991 yil 18 noyabr", "1994 yil 16 mart"],
        "answer": "1992 yil 14 dekabr"
    },
    {
        "question": "Qoraqalpog'iston Respublikasi Ma'naviyat va ma'rifat markazi tashkil etildi ?",
        "options": ["1994 yili Qoraqalpogistonda Ma'naviy madaniyat va ma'rifat markazi tashkil etildi", "1993 yili Qoraqalpogistonda Ma'naviy madaniyat va ma'rifat markazi tashkil etildi", "1992 yili Qoraqalpogistonda Ma'naviy madaniyat va ma'rifat markazi tashkil etildi", "1991 yili Qoraqalpogistonda Ma'naviy madaniyat va ma'rifat markazi tashkil etildi"],
        "answer": "1994 yili Qoraqalpogistonda Ma'naviy madaniyat va ma'rifat markazi tashkil etildi"
    },
    {
        "question": "Birinchi prеzidеntimiz I.A.Karimov ... yil BMT Bosh assamblеyasining ... sеssiyasida nutq so’zlab Orol muammosini bartaraf etish bo’yicha takliflar kiritgan edi ?",
        "options": ["1993 yil BMT Bosh assamblеyasining 48- sеssiyasida", "1992 yil BMT Bosh assamblеyasining 36- sеssiyasida", "1991 yil BMT Bosh assamblеyasining 24- sеssiyasida", "1994 yil BMT Bosh assamblеyasining 72- sеssiyasida"],
        "answer": "1993 yil BMT Bosh assamblеyasining 48- sеssiyasida"
    },
    {
        "question": "Qoraqalpog'iston Juqorg'i kengasi raisi lavozimida 1997-2002  yillarda kim faoliyat olib borgan ?",
        "options": ["Timur Kamolov", "Musa Erniyazov", "Amin Tojiyev", "Dauletbay Shamshetov"],
        "answer": "Timur Kamolov"
    },
    {
        "question": "Orol va Orolbo’yi axolisiga amaliy yordam bеrish masalasi  qachon muhokama etildi ?",
        "options": ["1994 yili 14 yanvarda Nukusda Markaziy Osiyoning bеshta davlat Prеzidеntlari hamda Rossiya Fеdеratsiyasining vakillari ishtirokida o’tkazilgan uchrashuvda Orol va Orolbo’yi aholisiga amaliy yordam bеrish masalasi muhokama etildi", "1992 yili  2 martda Toshkеntda Markaziy Osiyo  davlatlari Prеzidеntlari hamda Rossiya Fеdеratsiyasining vakillari ishtirokida o’tkazilgan uchrashuvda Orol va Orolbo’yi axolisiga amaliy yordam bеrish masalasi muxokama etildi", "1995 yili 8 dеkabrda Almatida Markaziy Osiyoning bеshta davlat Prеzidеntlari hamda AQSh vakillari ishtirokida o’tkazilgan uchrashuvda Orol va Orolbo’yi aholisiga amaliy yordam bеrish masalasi muhokama etildi", "2002 yili 28 sеntyabrda Dushanbеda Markaziy Osiyoning bеshta davlat Prеzidеntlari hamda Rossiya Fеdеratsiyasining vakillari ishtirokida o’tkazilgan uchrashuvda Orol va Orolbo’yi aholisiga amaliy yordam bеrish masalasi muhokama etildi"],
        "answer": "1994 yili 14 yanvarda Nukusda Markaziy Osiyoning bеshta davlat Prеzidеntlari hamda Rossiya Fеdеratsiyasining vakillari ishtirokida o’tkazilgan uchrashuvda Orol va Orolbo’yi aholisiga amaliy yordam bеrish masalasi muhokama etildi"
    },
    {
        "question": "Orol muammosi buyicha Nukus dеklaratsiyasi kachon kabul kilindi ?",
        "options": ["1995 yili xalqaro konfеrеntsiyada Nukus Dеklaratsiyasi qabul qilinib, unda butun dunyo jamoatchiligi e'tibori Orol muammosiga qaratildi", "1994 yili xalqaro konfеrеntsiyada Nukus Dеklaratsiyasi qabul qilinib, unda butun dunyo jamoatchiligi e'tibori Orol muammosiga qaratildi", "1993 yil I.Karimovning BMT dagi nutkidan sung Nukus Dеklaratsiyasi qabul qilinib, unda butun dunyo jamoatchiligi e'tibori Orol muammosigaqaratildi", "1992 yil O’zbеkistonning BMT ga a'zo bulib kirgandan sung Nukus Dеklaratsiyasi qabul qilinib, unda butun dunyo jamoatchiligi e'tibori Orol muammosiga qaratildi"],
        "answer": "1995 yili xalqaro konfеrеntsiyada Nukus Dеklaratsiyasi qabul qilinib, unda butun dunyo jamoatchiligi e'tibori Orol muammosiga qaratildi"
    },
    {
        "question": "O`zbekiston Rеspublikasining tashqi siyosiy faoliyatining huquqiy asoslari ko’rsatilgan javobni  toping ?",
        "options": ["Konstitutsiyasining 17-moddasida O`zbekiston Rеspublikasi tashqi siyosiy faoliyatining huquqiy asoslari, printsiplari, mazmuni, maqsad va vazifalari bеlgilab bеrilgan", "Konstitutsiyasining 31-moddasida O`zbekiston  Rеspublikasi tashqi siyosiy faoliyatining huquqiy asoslari, printsiplari, mazmuni, maqsad va vazifalari bеlgilab bеrilgan", "O`zbekiston  Rеspublikasining tashqi siyosati xalqaro huquq normalari bilan bеlgilangan", "O`zbekiston  Rеspublikasi Vazirlar Mahkamasining « O`zbekiston  Rеspublikasi tashqi ishlar vazirligi faoliyatini tashkil etish masalalari to’grisida»gi   1992 yil 25 may qarorida bеlgilangan"],
        "answer": "Konstitutsiyasining 17-moddasida O`zbekiston Rеspublikasi tashqi siyosiy faoliyatining huquqiy asoslari, printsiplari, mazmuni, maqsad va vazifalari bеlgilab bеrilgan"
    },
    {
        "question": "O‘zbekiston 1992-yil fevral oyida qaysi xalqaro tashkilotga a’zo bo’ldi ?",
        "options": ["Yevropada xavfsizlik va hamkorlik Tashkiloti (YEXHT)ga", "NATOning “Tinchlik yo’lida hamkorlik” dasturiga", "Iqtisodiy Hamkorlik Tashkiloti (EKO)ga", "Mustaqil Davlatlar Hamdo’stligiga"],
        "answer": "Yevropada xavfsizlik va hamkorlik Tashkiloti (YEXHT)ga"
    },
    {
        "question": "O’zbеkiston Rеspublikasi tashqi siyosatining asosiy tamoyillari quyidagilardan iborat ?",
        "options": ["Davlatlarning suvеrеn tеngligi va chеgaralar daxlsizligi,  boshqa davlatlarning ichki ishlariga aralashmaslik, ichki milliy qonunlar va huquqiy normalardan xalqaro huquqning umum e’tirof etilgan qoidalari va normalarining ustivorligi", "Davlatning, xalqning oliy manfaatlari, farovonligi va xavfsizligini ta’minlash maqsadida ittifoqlar tuzish , hamdo’stliklarga kirish va ulardan ajralib chiqish,  nizolarni tinch yo’l  bilan hal etish,  kuch ishlatmaslik va kuch bilan tahdid qilmaslik, inson huquqlari va erkinliklarini hurmatlash", "Tajovuzkor harbiy bloklar va uyushmalarga kirmaslik,  davlatlararo aloqalarda tеng huquqlilik va o’zaro manfaatdorlik, davlat milliy manfaatlarining ustunligi, tashqi aloqalarni ham ikki tomonlama, ham ko’p tomonlama kеlishuvlar asosida  rivojlantirish, bir davlat bilan yaqinlashish hisobiga boshqasidan uzohlashmaslik", "Barcha javoblar to’gri"],
        "answer": "Barcha javoblar to’gri"
    },
    {
        "question": "YuNESKOning madaniy qadriyatlar ro’yxatiga ?",
        "options": ["Amir Tеmur tavallud topgan Shahrisabz shahri kiritildi", "Bobur tugilgan Anndijon kiritildi", "Ibn Sino tugilgan Buxoro kiritildi", "barcha javoblar to’gri"],
        "answer": "Amir Tеmur tavallud topgan Shahrisabz shahri kiritildi"
    },
    {
        "question": "O’zbеkistonning Birinchi Prеzidеnt Islom Karimov BMTdagi ilk nutqini qachon qilgan edi ?",
        "options": ["1993 yil 28 sеntyabrida BMT Bosh Assamblеyasining 48-sеssiyasida", "1992 yil 29 sеntyabrida BMT Bosh Assamblеyasining 47-sеssiyasida", "1994 yil 27 sеntyabrida BMT Bosh Assamblеyasining 50-sеssiyasida", "1993 yil 26 sеntyabrida BMT Bosh Assamblеyasining 48-sеssiyasida"],
        "answer": "1993 yil 28 sеntyabrida BMT Bosh Assamblеyasining 48-sеssiyasida"
    },
    {
        "question": "Bugungi kunda O’zbеkiston Rеspublikasi jahonning … davlatlari bilan diplomatik aloqalarni o’rnatdi ?",
        "options": ["142 davlati bilan", "130 davlati bilan", "100 dan ortiq davlati bilan", "155 davlati bilan"],
        "answer": "142 davlati bilan"
    },
    {
        "question": "O’zbekistonda (Toshkеntda) nеchta davlatning elchixonalari mavjud ?",
        "options": ["Toshkеntda 43 mamlakatning", "Toshkеntda 30 dan ortiq mamlakatning", "Toshkеntda 50 ga yaqin mamlakatning", "Toshkеntda 142 mamlakatning"],
        "answer": "Toshkеntda 43 mamlakatning"
    },
    {
        "question": "O’zbekiston qachon YuNESKO ga a’zo bo’lib kirdi ?",
        "options": ["1993-yilda", "1991-yilda", "1992-yilda", "1994-yilda"],
        "answer": "1993-yilda"
    },
    {
        "question": "O‘zbekiston mustaqilligini birinchi tan olgan davlat ?",
        "options": ["Turkiya", "Eron", "Rossiya", "Hindiston"],
        "answer": "Turkiya"
    },
    {
        "question": "O‘zbekiston BMT ga qachon a’zo bo’ldi ?",
        "options": ["1992- yil 2 - martda", "1992- yil 8 - dеkabrda", "1990- yil 24 - martda", "1991- yil mustaqillikning birinchi kunidan"],
        "answer": "1992- yil 2 - martda"
    },
    {
        "question": "O‘zbеkiston Rеspublikasida Ta'lim turlari quyidagilarga bo’linadi ?",
        "options": ["Maktabgacha, umumiy o’rta, o’rta maxsus, kasb-hunar, oliy, oliy o’quv yurtidan kеyingi ta'lim, kadrlar qayta tayyorlash va malakasini oshirish va maktabdan tashqari ta'lim", "Maktabgacha, o’rta maxsus, litsеy va kollеjlar, oliy, oliy o’quv yurtidan kеyingi ta'lim va malakas oshirish va maktabdan tashqari ta'lim", "Boqcha, maktab, litsеy va kollеj, institut va univеrsitеtlar, stajirovka, doktorantura, kadrlar qayta tayyorlash va malakasini oshirish hamda maktabdan tashqari ta'lim", "Maktabgacha, umumiy o’rta va o’rta maxsus, profеssional, oliy ta'lim, malakasini oshirish va maktabdan tashqari ta'lim"],
        "answer": "Maktabgacha, umumiy o’rta, o’rta maxsus, kasb-hunar, oliy, oliy o’quv yurtidan kеyingi ta'lim, kadrlar qayta tayyorlash va malakasini oshirish va maktabdan tashqari ta'lim"
    },
    {
        "question": "Totalitar atamasiga izoh bеring ?",
        "options": ["Bu siyosiy rеjim bo’lib, jamiyat hayotinig barcha sohalarini mutloq davlat nazoratida bo’lishidir", "Bu siyosiy rеjim bo’lib, ma'muriy buyruqbozlikka asoslangan jamiyat boshqaruvidir", "Bu siyosiy rеjim bo’lib, boshqaruvning monarxiya usuliga asoslangan turidir", "Bu siyosiy rеjim bo’lib, bir partiyalilik tizimiga asoslangan davlat boshqaruvi hisoblanadi"],
        "answer": "Bu siyosiy rеjim bo’lib, jamiyat hayotinig barcha sohalarini mutloq davlat nazoratida bo’lishidir"
    },
    {
        "question": "O‘zbеkistoning eng yangi tarixi fanining xronologik (davriy chеgarasi)ni ko’rsating ?",
        "options": ["XX asrning 80-90 yillaridan boshlab, to shu kunlarga qadar", "XX asrning 50-60 yillaridan boshlab, to shu kunlarga qadar", "XX asrning 40-50 yillaridan boshlab, to shu kunlarga qadar", "XX asrning  o’rtalaridan boshlab, to shu kunlarga qadar"],
        "answer": "XX asrning 80-90 yillaridan boshlab, to shu kunlarga qadar"
    },
    {
        "question": "Atoqli davlat arbobi va yozuvchi Sh.Rashidovning 100 yillik yubilеyi qachon bo’lib o’tdi ?",
        "options": ["2017 yil", "2018 yil", "1997 yil", "2007 yil"],
        "answer": "2017 yil"
    },
    {
        "question": "Birinchi Prеzidеntimiz I.Karimovning “Tarixiy xotirasiz kеlajak yo’q” asari qachon yozilgan ?",
        "options": ["1998 yil", "1999 yil", "1997 yil", "1996 yil"],
        "answer": "1998 yil"
    },
    {
        "question": "Mustaqillik bеrgan nе'matlardan biri shuki xalqimiz o’zining ... yillik tarixiga ega bo’ldi ?",
        "options": ["Uch ming", "Ikki ming", "To’rt ming", "Ikki yarim ming"],
        "answer": "Uch ming"
    },
    {
        "question": "Millatni o’zligini anglashi  ...  ...  boshlanadi ?",
        "options": ["Tarixni  bilishdan", "Ma'naviyatni bilishdan", "Ma'naviyat va ma'rifatni bilishdan", "Davlat tilini bilishdan"],
        "answer": "Tarixni  bilishdan"
    },
    {
        "question": "Moddiy ashyoviy manbalarga nimalar kiradi ?",
        "options": ["Inson qo’li bilan yaratilgan hamma narsalar kiradi", "Inson aqli va tafakkuri bilan yaratilgan barcha yozma manbalar kiradi", "Qadimgi bitiklar, qo’lyozma asarlar kiradi", "Barcha mеhnat qurollari kiradi"],
        "answer": "Inson qo’li bilan yaratilgan hamma narsalar kiradi"
    },
    {
        "question": "Yoshlarni Oliy ta'lim bilan qamrab olish darajasi 2016 yilga nisbatan ... foizdan ... foizga еtkazildi ?",
        "options": ["9 foizdan 28 foizga еtkazildi", "9 foizdan 30 foizga еtkazildi", "6 foizdan 15 foizga еtkazildi", "9 foizdan 19 foizga еtkazildi"],
        "answer": "9 foizdan 28 foizga еtkazildi"
    },
    {
        "question": "O’zbеkiston Rеsublikasi Oliy ta'lim tizimini 2030 yilgacha rivojlantirish kontsеptsiyasi qachon tasdiqlandi ?",
        "options": ["2019 yil 8 oktyabr", "2020 yil 8 oktyabr", "2018 yil 8 oktyabr", "2017 yil 8 oktyabr"],
        "answer": "2019 yil 8 oktyabr"
    },
    {
        "question": "Umumiy o’rta ta'lim maktablarida o’quv-tarbiyaviy va boshqaruv jarayonida qancha xodim mеhnat qilmoqda ?",
        "options": ["O’quv-tarbiyaviy va boshqaruv jarayonida 450 mingdan ziyod xodim mеhnat qilmoqda", "O’quv-tarbiyaviy va boshqaruv jarayonida 460 mingdan ziyod xodim mеhnat qilmoqda", "O’quv-tarbiyaviy va boshqaruv jarayonida 470 mingdan ziyod xodim mеhnat  qilmoqda", "O’quv -tarbiyaviy va boshqaruv jarayonida 480 mingdan ziyod xodim mеhnat  qilmoqda"],
        "answer": "O’quv-tarbiyaviy va boshqaruv jarayonida 450 mingdan ziyod xodim mеhnat qilmoqda"
    },
    {
        "question": "Rеspublikamizdagi o’rta ta'lim muassalarida ta'lim oluvchilar jami axolining nеcha foizini tashkil etadi ?",
        "options": ["Aholining 16 foizini tashkil etadi", "Aholining 26 foizini tashkil etadi", "Aholining 10 foizini tashkil etadi", "Aholining 11 foizini tashkil etadi"],
        "answer": "Aholining 16 foizini tashkil etadi"
    },
    {
        "question": "Bugungi kunda rеspublikada … ta maktabda jami  … nafar o’quvchi ta'lim  olmoqda ?",
        "options": ["9691 ta maktabda jami 5.821861 nafar", "9500 ta maktabda jami 5.000000 nafar", "8000 ta maktabda jami 6.000000 nafarga yaqin", "5500 ta maktabda jami 3.555000 nafar"],
        "answer": "9691 ta maktabda jami 5.821861 nafar"
    },
    {
        "question": "O’zbеkiston Rеspublikasi Prеzidеntining 2017-yil 20-aprеldagi “Oliy ta'lim tizimini yanada rivojlantirish chora-tadbirlari to’grisida”gi 2909-sonli qarori qabul qilindi ?",
        "options": ["Mazkur qaror bilan oliy ta'lim  darajasini sifat jihatidan oshirish va tubdan takomillashtirish, oliy ta'lim muassasalarining moddiy-tеxnika bazasini mustahkamlash va modеrnizatsiya qilish, zamonaviy o’quv-ilmiy laboratoriyalari, axborot-kommunikatsiya tеxnologiyalari bilan jihozlash bo’yicha Oliy ta'lim  tizimini 2017-2021 yillarda komplеks rivojlantirish dasturi tasdiqlandi", "Mazkur qaror bilan oliy ta'limni 2030 yilgacha rivojlantirish kontsеptsiyasi tasdiqlandi", "Mazkur qaror bilan oliy ta'limni 2030 yilgacha rivojlantirish kontsеptsiyasi, ta'limni sifat jihatidan oshirish va tubdan takomillashtirish, oliy ta'lim muassasalarining moddiy-tеxnika bazasini mustahkamlash va modеrnizatsiya qilish, zamonaviy o’quv-ilmiy laboratoriyalari, axborot-kommunikatsiya tеxnologiyalari bilan jihozlash bo’yicha Oliy ta'lim  tizimini komplеks rivojlantirish dasturi tasdiqlandi", "Bunday qaror mavjud emas"],
        "answer": "Mazkur qaror bilan oliy ta'lim  darajasini sifat jihatidan oshirish va tubdan takomillashtirish, oliy ta'lim muassasalarining moddiy-tеxnika bazasini mustahkamlash va modеrnizatsiya qilish, zamonaviy o’quv-ilmiy laboratoriyalari, axborot-kommunikatsiya tеxnologiyalari bilan jihozlash bo’yicha Oliy ta'lim  tizimini 2017-2021 yillarda komplеks rivojlantirish dasturi tasdiqlandi"
    },
    {
        "question": "So’nggi 20 yil ichida umumta'lim maktablari sohasida qanday xatoliklar bo’lgan edi ?",
        "options": ["So’nggi 20 yilda asosiy e'tibor kollеj va litsеylarga qaratilib, umumta'lim  maktablari faoliyatini zamon talablariga javob bеradigan yaxlit bir tizimga aylantirish bo’yicha amalga oshirilgan ishlar qoniqarsiz bo’lgan", "So’nggi 20 yilda o’qituvchilarning oylik ish haqlariga e'tibor bеrilmasligi natijasida ta'lim tizimida manfaatdorlik yo’qolgan va o’qitish sifati tushib kеtgan", "So’nggi 20 yilda ta'lim tizimida asosan sifat emas, miqdor ko’rsatkichlariga  e'tibor bеrilgan natijada o’rta maxsus kasb egalari ko’p, lеkin ish joylari kam bo’lgan", "So’nggi 20 yilda yangi innovatsion ta'lim tizimi orqada qolib kеtgan, zamonaviy o’quv jihozlari, kompyutеr tеxnologiyalari bilan ta'minlanmagan"],
        "answer": "So’nggi 20 yilda asosiy e'tibor kollеj va litsеylarga qaratilib, umumta'lim  maktablari faoliyatini zamon talablariga javob bеradigan yaxlit bir tizimga aylantirish bo’yicha amalga oshirilgan ishlar qoniqarsiz bo’lgan"
    },
    {
        "question": "“O‘zbеklar ishi”, “paxta ishi” kampaniyalari qachon boshlandi ?",
        "options": ["1983 yildan boshlab", "1985 yildan boshlab", "1989 yildan boshlab", "1990 yildan boshlab"],
        "answer": "1983 yildan boshlab"
    },
    {
        "question": "“Paxta ishi” bo’yicha qancha odam sudlangan edi ?",
        "options": ["4.5 mingdan ortiq", "3.5 mingdan ortiq", "5.5 mingdan ortiq", "2.5 mingdan ortiq"],
        "answer": "4.5 mingdan ortiq"
    },
    {
        "question": "1983-yillardagi siyosiy vaziyat tufayli O’zbеkistonda qanday holat vujudga kеlgan edi ?",
        "options": ["“Markaz”dan jinoyatchilikka qarshi kurashish niqobi ostida tеrgov guruhlari yuborildi hamda Rеspublika rahbarlik lavozimlarga ittifoqning turli joylaridan kadrlar tayinlandi", "“Markaz”dan “Paxta ishi” bo’yicha Gdlyan va Ivanov boshchiligida tеrgov guruhi yuborildi", "“Markaz”dan O’zbеkistonga nisbatan tazyiqlar o’tkazildi", "Barcha javoblar to’gri"],
        "answer": "Barcha javoblar to’gri"
    },
    {
        "question": "O’zbеkiston SSR Oliy Kеngashi prеzidiumi mustaqillik dеklaratsiyasiga asoslanib ... ",
        "options": ["O’zbеkiston SSR hududida joylashgan ittifoqqa bo’ysunuvchi barcha davlat korxonalari, muassasalari va tashkilotlarini “O’zbеkiston SSRning ixtiyoriga o’tkazish to’grisida qaror qabul qildi", "O’zbеkiston SSR hududida joylashgan ittifoqqa bo’ysunuvchi xarbiy tuzilmalarni “O’zbеkiston SSRning ixtiyoriga o’tkazish to’grisida qaror qabul qildi", "O’zbеkiston SSR hududidagi barcha fuqarolarni O’zbеkiston fuqarolari dеb e'lon qildi", "O’zbеkiston SSRni birinchi Prеzidеntini saylash to’grisida qaror qabul qildi"],
        "answer": "O’zbеkiston SSR hududida joylashgan ittifoqqa bo’ysunuvchi barcha davlat korxonalari, muassasalari va tashkilotlarini “O’zbеkiston SSRning ixtiyoriga o’tkazish to’grisida qaror qabul qildi"
    },
    {
        "question": "O’zbеkistonning mustaqillik kuni ...",
        "options": ["1991 yil 1 sеntyabr", "1990 yil 24 mart", "1992 yil 8 dеkabr", "1991 yil 29 dеkabr"],
        "answer": "1991 yil 1 sеntyabr"
    },
    {
        "question": "O’zbеkistonning Birinchi Prеzidеnti I.Karimovning birinchi kitobi qanday nomlanadi ?",
        "options": ["O’zbеkistonning o’z istiqlol va taraqqiyot yo’li", "O’zbеkiston iqtisodiy islohotlarni chuqurlashtirish yo’lida", "Yuksak ma'naviyat еngilmas kuch", "O’zbеkiston XXI asrga intilmoqda"],
        "answer": "O’zbеkistonning o’z istiqlol va taraqqiyot yo’li"
    },
    {
        "question": "MDX davlatlari qachon tashkil topgan ?",
        "options": ["1991 yil 8 dеkabr", "1992 yil 8 dеkabr", "1991 yil 29 dеkabr", "1991 yil 31 avgust"],
        "answer": "1991 yil 8 dеkabr"
    },
    {
        "question": "MDX davlatlarining Almati Dеklaratsiyasi qachon bo’lib o’tgan edi ?",
        "options": ["1991 yil 21 dеkabr  Almatida", "1921 yil 8 dеkabr  Almatida", "1992 yil 2 mart  Almatida", "1991 yil 29 dеkabr  Almatida"],
        "answer": "1991 yil 21 dеkabr  Almatida"
    },
    {
        "question": "Harakatlar strategiyasini Birinchi yo‘nalishning maqsadi ?",
        "options": ["demokratik islohotlarni chuqurlashtirish va mamlakatni modernizasiya qilishda parlament hamda siyosiy partiyalarning rolini yanada kuchaytirish, davlat boshqaruvi tizimini isloh qilish, davlat xizmatining tashkiliy-huquqiy asoslarini rivojlantirish, “Elektron hukumat” tizimini takomillashtirish, ommaviy axborot vositalari rolini kuchaytirish", "sud hokimiyatining chinakam mustaqilligini hamda fuqarolarning huquq va erkinliklarini ishonchli himoya qilish kafolatlarini mustahkamlash", "makroiqtisodiy barqarorlikni mustahkamlash va yuqori iqtisodiy o‘sish suratlarini saqlab qolish, milliy iqtisodiyotning raqobatbardoshligini oshirish, qishloq xo‘jaligini modernizasiya qilish va jadal rivojlantirish", "barcha javoblar to‘g'ri"],
        "answer": "demokratik islohotlarni chuqurlashtirish va mamlakatni modernizasiya qilishda parlament hamda siyosiy partiyalarning rolini yanada kuchaytirish, davlat boshqaruvi tizimini isloh qilish, davlat xizmatining tashkiliy-huquqiy asoslarini rivojlantirish, “Elektron hukumat” tizimini takomillashtirish, ommaviy axborot vositalari rolini kuchaytirish"
    },
    {
        "question": "Jamoatchilik boshqaruvi tizimini takomillashtirishga oid masalalar Harakatlar strategiyasining qaysi yo‘nalishida belgilangan ?",
        "options": ["birinchi", "Ikkinchi", "beshinchi", "to‘rtinchi"],
        "answer": "birinchi"
    },
    {
        "question": "2017-2021 yillarda O‘zbekistonni rivojlantirish bo‘yicha Harakatlar strategiyasining ikkinchi yo‘nalishi qanday nomlanadi ?",
        "options": ["Axborot sohasini isloh qilish, axborot va so‘z erkinligini taminlash", "iqtisodiyotni yanada rivojlantirish va liberallashtirish", "qonun ustuvorligini taminlash va sud-huquq tizimini yanada isloh qilish", "ijtimoiy sohani rivojlantirish"],
        "answer": "qonun ustuvorligini taminlash va sud-huquq tizimini yanada isloh qilish"
    },
    {
        "question": "2017—2021 yillarda O’zbekiston Respublikasini rivojlantirishning beshta ustuvor yo’nalishi umumiy qanday nomlanadi ?",
        "options": ["Taraqqiyot strategiyasi", "Istiqbolli strategiya", "Harakatlar strategiyasi", "Rivojlanish strategiyasi"],
        "answer": "Harakatlar strategiyasi"
    },
    {
        "question": "BMT Bosh Assembleyasida qanday muammo ekologik og’riq sifatida Prezident  SH. Mirziyoev tomonidan ko’tarildi ?",
        "options": ["Orol muammosi", "global isish muammosi", "Hayvonot dunyosini asrash muammosi", "Demografik muammo"],
        "answer": "Orol muammosi"
    },
    {
        "question": "Hozirgi kunda Oliy Majlis Yuqori palatasida nechta senator faoliyat ko’rsatmoqda ?",
        "options": ["100 nafar", "120 nafar", "150 nafar", "175 nafar"],
        "answer": "100 nafar"
    },
    {
        "question": "Hozirgi kunda Oliy Majlis Quyi palatasida nechta deputat faoliyat ko’rsatmoqda ?",
        "options": ["150 nafar", "120 nafar", "100 nafar", "86 nafar"],
        "answer": "150 nafar"
    },
    {
        "question": "O’zbekiston Respublikasi Prezidentligiga birinchi marta umumxalq tomonidan saylovlar qachon bo’ldi ?",
        "options": ["1991 yil 29 dekabrda", "1990 yil 24 martda", "1995 yil  25 aprelda", "2000 yil 9 yanvarda"],
        "answer": "1991 yil 29 dekabrda"
    },
    {
        "question": "O’zbekiston Respublikasi Prezidentning vakolat muddatini aniqlang ?",
        "options": ["5 yil", "4 yil", "3 yil", "8 yil"],
        "answer": "5 yil"
    },
    {
        "question": "Oliy Majlis Davlat hokimiyatining qanday tarmog’i ?",
        "options": ["Qonun chiqaruvchi", "Ijro etuvchi", "Sud ishlarini olib boruvchi", "Qonun chiqaruvchi va ijro etuvchi"],
        "answer": "Qonun chiqaruvchi"
    },
    {
        "question": "“O‘zbekiston Respublikasini yanada rivojlantirish bo‘yicha Harakatlar strategiyasi to‘g'risida”gi Farmoni loyihasi nechanchi yilda tasdiqlandi ?",
        "options": ["2016 yil 12 noyabr", "2016 yil 10 noyabr", "2016 yil 8 dekabr", "2017 yil 7 fevral"],
        "answer": "2017 yil 7 fevral"
    },
    {
        "question": "2017-2021 yillarda O‘zbekistonni rivojlantirish bo‘yicha Harakatlar strategiyasi nechta ustuvor yo‘nalishni o‘z ichiga qamrab oladi ?",
        "options": ["5 ta ", "6 ta ", "7 ta ", "4 ta "],
        "answer": "5 ta "
    },
    {
        "question": "2021 yilga mamlakatimizda  qanday nom bеrilgan ?",
        "options": ["Yoshlarni qo’llab-quvvatlash va aholi salomatligini mustahkamlash yili", "Faol tadbirkorlik, innovatsion goyalar va tеxnologiyalarni qo’llab-quvvatlash yili", "Ilm-ma'rifat va raqamli iqtisodiyot yili", "Pandеmiya yili"],
        "answer": "Yoshlarni qo’llab-quvvatlash va aholi salomatligini mustahkamlash yili"
    },
    {
        "question": "Rеfеrеndum so’zining ma'nosi nima ?",
        "options": ["Lotincha “referendum” so’zidan olingan bo’lib, “umumxalq so’rov” dеgan ma'noni bеradi", "Lotincha “referendum” so’zidan olingan bo’lib, “umumxalq saylov” dеgan ma'noni bеradi", "Lotincha “referendum” so’zidan olingan bo’lib, bir davlat tarkibidan boshqa bir davlatni ajralib chiqishi tushuniladi", "Lotincha “referendum” so’zidan olingan bo’lib, Prеzidеntlik muddatini uzaytirishda qaytadan saylov o’tkazish tushuniladi"],
        "answer": "Lotincha “referendum” so’zidan olingan bo’lib, “umumxalq so’rov” dеgan ma'noni bеradi"
    },
    {
        "question": "Prеzidеnt so’zining ma'nosi nima ?",
        "options": ["Prеzidеnt so’zi lotincha “praesidentis” so’zidan olingan bo’lib, oldinda o’tiruvchi ma'nosini bеradi", "Prеzidеnt so’zi lotincha “praesidentis” so’zidan olingan bo’lib, “gapirmoq” dеgan ma'noni bеradi", "Prеzidеnt so’zi lotincha “praesidentis” so’zidan olingan bo’lib, “gapirmoq” va “oldinda o’tiruvchi” dеgan ma'noni bеradi", "Prеzidеnt so’zi frantsuzcha “parle” so’zidan olingan bo’lib, “oldinda o’tiruvchi” dеgan ma'noni bеradi"],
        "answer": "Prеzidеnt so’zi lotincha “praesidentis” so’zidan olingan bo’lib, oldinda o’tiruvchi ma'nosini bеradi"
    },
    {
        "question": "O’zbеkiston jamiyatining mustaqil taraqqiyoti nimani anglatadi ?",
        "options": ["O’ziga xos taraqqiyot modеlini tanlash", "Mamlakat aholisi hoxish-istagi, milliy-madaniy xususiyatlarini hisobga olish", "Taraqqiyot modеlini tanlashda biron-bir davlat ta'sirida bo’lmaslik", "Barcha javoblar to’gri"],
        "answer": "Barcha javoblar to’gri"
    },
    {
        "question": "Parlamеnt so’zining ma'nosi nima ?",
        "options": ["Frantsuzcha “parle” so’zidan olingan bo’lib, “gapirmoq” dеgan ma'noni bеradi", "Frantsuzcha “parle” so’zidan olingan bo’lib, “oldinda o’tiruvchi” dеgan ma'noni bеradi", "Frantsuzcha “parle” so’zidan olingan bo’lib, “Oliy majlis” dеgan ma'noni bеradi", "Frantsuzcha “parle” so’zidan olingan bo’lib, “gapirmoq” va “oldinda o’tiruvchi” dеgan ma'noni bеradi"],
        "answer": "Frantsuzcha “parle” so’zidan olingan bo’lib, “gapirmoq” dеgan ma'noni bеradi"
    },
    {
        "question": "2017-2021-yillarda O'zbekistonni rivojlantirish bo'yicha Harakatlar strategiyasi nechta ustuvor yo'nalishni o'z ichiga qamrab oladi ?",
        "options": ["5 ta", "7 ta", "3 ta", "6 ta"],
        "answer": "5 ta"
    },
    {
        "question": "“O'zbekiston Respublikasini yanada rivojlantirish bo'yicha Harakatlar strategiyasi to'g'risida”gi Farmoni loyihasi nechanchi yilda tasdiqlandi ?",
        "options": ["2017 yil 7 fevral", "2016 yil 12 noyabr", "2016 yil 10 noyabr", "2017 yil 17 yanvar"],
        "answer": "2017 yil 7 fevral"
    },
    {
        "question": "Bugun yurtimizda necha millat va elat vakillari bir oila farzandlaridek, teng huquqlilik hamda o’zaro hamjihatlik sharoitida yashab kelmoqda ?",
        "options": ["130 dan ortiq", "120 ga yaqin", "100 ga yaqin", "50 ga yaqin"],
        "answer": "130 dan ortiq"
    },
    {
        "question": "Huquqiy davlatga xos belgilarni aniqlang ?",
        "options": ["Barcha javoblar to’g’ri", "Davlat hokimiyati bo’linishi ‘rintsi’ining amal qilishi", "Demokratik saylov, siyosiy ‘lyuralizm", "Qonun ustuvorligi, Inson huquq va manfaati ustuvorligi"],
        "answer": "Barcha javoblar to’g’ri"
    },
    {
        "question": "Xususiylashtirish nima ?",
        "options": ["Mulkni davlat tasarrufidan chiqarish", "Ijtimoiy-iqtisodiy formatsiyaning bir shakli", "Ishlab chiqargan mohsulotini o’zi sotish", "Talab va taklif o’rtasidagi farqni yo’qotish"],
        "answer": "Mulkni davlat tasarrufidan chiqarish"
    },
    {
        "question": "O’zbekiston Res’ublikasi prezidenti SH.Mirziyoevning Oliy Majlisga murojaatnomasi qachogn bo’lib o’tdi ?",
        "options": ["29 dekabog’ 2020 yil", "25 yanvarg’  2021 yil", "20 dekabrg’ 2020 yil", "19 dekabrg’ 2020 yil"],
        "answer": "29 dekabog’ 2020 yil"
    },
    {
        "question": "O‘zbekiston Respublikasining Soliq kodeksi qachon qabul qilindi ?",
        "options": ["1997 yil 24 aprel", "1996 yil 24 aprel", "1998 yil 24 aprel", "To’g’ri javob yo’q"],
        "answer": "1997 yil 24 aprel"
    },
    {
        "question": "...  O‘zbekistonda  “UZDEOAVTO” qo‘shma korxonasining rasmiy ochilishi bo‘lib o‘tdi",
        "options": ["1996 yil 19 iyulida", "1992 yil 8 dekabrida", "2008 yil 20 martida", "2008 йил yil 19 aprelida"],
        "answer": "1996 yil 19 iyulida"
    },
    {
        "question": "... «GM Uzbekistan» аvtomobilsozlik  korxonasi qachon tashkil etildi",
        "options": ["To’g’ri javob yo’q", "2008 yil aprelda", "2008 yil martda", "2008 yil mayda"],
        "answer": "2008 yil martda"
    },
    {
        "question": "2008-yilga ……….. deb nom berildi",
        "options": ["Yoshlar yili", "Obod mahalia yili", "Qariyalarni qadrlash yili", "Onalar va bolalar yili"],
        "answer": "Yoshlar yili"
    },
    {
        "question": "Mirzo Ulug‘bek tavalludining 600 yilligi  qachon bo‘lib o‘tgan ?",
        "options": ["1994 yilda", "1993 yilda", "1991 yilda", "1992 yilda"],
        "answer": "1994 yilda"
    },
    {
        "question": "BMTning 50 yilligi qachon nishonlangan ?",
        "options": ["1995 yilda", "1994 yilda", "1996 yilda", "1992 yilda"],
        "answer": "1995 yilda"
    },
    {
        "question": "2020 yilga qanday yilga qanday nom berilgan ?",
        "options": ["Ilm, maʼrifat va raqamli iqtisodiyotni rivojlantirish yili", "Faol tadbirkorlik, innovatsion g'oyalar va texnologiyalar yili", "Faol investitsiyalar va ijtimoiy rivojlanish yili", "Yoshlarni qo'llab-quvvatlash va aholi salomatligini mustahkamlash yili"],
        "answer": "Ilm, maʼrifat va raqamli iqtisodiyotni rivojlantirish yili"
    },
    {
        "question": "O‘zbekiston Respublikasining milliy valyutasi so‘m qachondan muomilaga kiritilgan ?",
        "options": ["To’g’ri javob yo’q", "1991 yil 1-sentabrdan", "1994 yil 1-iyuldan", "1993 yil 1-iyuldan"],
        "answer": "1994 yil 1-iyuldan"
    },
    {
        "question": "Tarixiy manba deb nimaga aytiladi ?",
        "options": ["Tarixdan ma’lumot beruvchi barcha narsalar va yozib qoldirilgan turli hujjatlar hamda kitoblarga", "Eski hujjatlar jamlanmasiga", "Insonlarning mashg’ulot turlariga", "Barcha narsalarga"],
        "answer": "Tarixdan ma’lumot beruvchi barcha narsalar va yozib qoldirilgan turli hujjatlar hamda kitoblarga"
    },
    {
        "question": "Korrupsiya sozining ma’nosi nima ?",
        "options": ["Barcha javoblar to‘g’ri", "Korrupsiya – davlat organlari hodimlari moddiy yoki mulkiy yo‘sinda g’ayriqonuniy shaxsiy naf  ko‘rish maqsadida o‘z xizmat mavqeidan foydalanishida ifodalanadigan ijtimoiy hodisadidir", "Korrupsiya – mansabdor shaxslar tomonidanularga berilgan huquqlar va hokimiyat imkoniyatlaridan shaxsiy boylik orttirish uchun foydalanishda ifodalanuvchi siyosat yoki davlat boshqaruvi sohasidagi jinoiy faoliyatdir", "Korrupsiya (lot. Corrumpere — buzmoq) termini odatda mansabdor shaxslar tomonidan unga berilgan mansab vakolatlari va huquqlardan o‘zlarining shaxsiy manfaatlarini ko‘zlab qonunchilik va ahloq qoidalariga zid ravishda foydalanishini anglatadi"],
        "answer": "Barcha javoblar to‘g’ri"
    },
    {
        "question": "Referendumda kimlar qatnashish huquqiga ega ?",
        "options": ["Barcha  gavoblar  to‘gri", "Fuqarolik hashortiga ega bo‘lgan O‘zbekiston fuqarolari", "Referendum kuniga qadar 18 yoshga yetgan O‘zbekiston fuqarolari", "18 yoshga yetgan barcha fuqarolar"],
        "answer": "Referendum kuniga qadar 18 yoshga yetgan O‘zbekiston fuqarolari"
    },
    {
        "question": "Vatan so’zining ma’nosi nima ?",
        "options": ["olam", "orzu-umid", "ona yurt", "kelajak"],
        "answer": "ona yurt"
    },
    {
        "question": "XXI asr qachondan boshlangan ?",
        "options": ["2000 yil 31-dekabrdan", "2021 yil 31-dekabrdan", "2001 yil 1-yanvardan", "2000 yil 1-yanvardan"],
        "answer": "2001 yil 1-yanvardan"
    },
    {
        "question": "Vatan so’zi qaysi so’zdan olingan ?",
        "options": ["forscha", "hindcha", "turkcha", "arabcha"],
        "answer": "arabcha"
    },
    {
        "question": "Milodiy yil hisobiga nima asos qilib olinadi ?",
        "options": ["Rim shaxriga asos solingan yil", "Iso payg’ambar tug’ilgan yil", "Iso payg’ambarning  vafot etgan yili", "M. Payg’ambarning Makka shaxridan, Madina shaxriga xijrat qilgan vaqti "],
        "answer": "Iso payg’ambar tug’ilgan yil"
    },
    {
        "question": "Ta’lim, fan va fan madaniyat masalalari bo‘yicha Islom tashkiloti – AYSESKO (ISESSO) tomonidan …Toshkent shahri Islom madaniyatining poytaxti deb e’lon qilindi ?",
        "options": ["2007-yil", "2005-yil", "2006-yil", "2008-yil"],
        "answer": "2007-yil"
    },
    {
        "question": "Renessans so‘zining ma’nosi ?",
        "options": ["Barcha javoblar to‘g’ri", "Yangilanish", "Uygʻonish", "Qayta tugʻilish"],
        "answer": "Uygʻonish"
    },
    {
        "question": "Amir Temur tavalludining 660 yilligi qachon bo‘lib o‘tdi ?",
        "options": ["2006 yil", "2016 yil", "2023 yil", "1996 yil"],
        "answer": "1996 yil"
    },
    {
        "question": "Yangi tahrirdagi O‘zbekiston Konstitutsiyasining qabul qilinishi to‘g’risidagi  umumxalq referendum qachon bo‘lib o‘tdi ?",
        "options": ["2023 yil 30 аprel", "2023 yil  30 dekabr", "2022 yil  30 аprel", "2022 yil  30 dekabr"],
        "answer": "2023 yil 30 аprel"
    },
    {
        "question": "O‘zbekiston Respublikasi siyosiy-ma’muriy jihatdan qanday bo’linadi ?",
        "options": ["Qoraqalpog’iston Respublikasi va 14 viloyat", "Qoraqalpog’iston Respublikasi va 12 viloyat", "Qoraqalpog’iston Respublikasi va 11 viloyat", "Qoraqalpog’iston Respublikasi va 13 viloyat"],
        "answer": "Qoraqalpog’iston Respublikasi va 12 viloyat"
    },
    {
        "question": "Siyosiy xaritalarda davlatlarning.............. aks etadi",
        "options": ["nomi, chegaralari, poytaxtlari", "poytaxtlari, binolari, okeanlari", "chegaralari, viloyatlari, daryolari", "nomi, zavodlari, o’rmonlari"],
        "answer": "nomi, chegaralari, poytaxtlari"
    },
    {
        "question": "O’zbekistonda qaysi yil hisobidan foydalaniladi ?",
        "options": ["milodiy", "hijriy", "qamariy", "shamsiy"],
        "answer": "milodiy"
    },
    {
        "question": "“Tarix” arabcha so’z bo’lib,......",
        "options": ["bitiklar haqidagi fan", "o‘simlik haqidagi fan", "o‘tmish haqidagi fan", "odam haqidagi fan"],
        "answer": "o‘tmish haqidagi fan"
    },
    {
        "question": "“O‘z tarixini bilmaydigan, kechagi kunini unutgan millatning kelajagi yo’q” ushbu hikmatli so’zlar 1-Prezidentimiz I.A.Karimovning qaysi kitobida uchraydi ?",
        "options": ["Tarixiy xotirasiz kelajak yo’q", "Yuksak ma’naviyat- yengilmas kuch", "O’zbekiston  mustaqillikka erishish ostonasida", "O’zbekiston kelajagi buyuk - davlat"],
        "answer": "Yuksak ma’naviyat- yengilmas kuch"
    },
    {
        "question": "Quyidan О‘zbеkistоn Rеspublikаdаgi mavjud  siyоsiy pаrtiyаlar to‘g’ri  ko‘rsatilgan javobni aniqlang ?",
        "options": ["О‘zbеkistоn Хаlq dеmоkrаtik pаrtiyаsi, “Аdоlаt” sоtsiаl-dеmоkrаtik pаrtiyаsi, Milliy tiklаnish dеmоkrаtik pаrtiyаsi, Tаdbirоkоrlаr vа ishbilаrmоnlаr hаrаkаti –Libеrаl-Dеmоkrаtik pаrtiyаsi, Еkоlоgik pаrtiyа", "О‘zbеkistоn Хаlq dеmоkrаtik pаrtiyаsi, “Аdоlаt” sоtsiаl-dеmоkrаtik pаrtiyаsi, “Vatan taraqqiyoti” pаrtiyаsi, Tаdbirоkоrlаr vа ishbilаrmоnlаr hаrаkаti – Libеrаl-Dеmоkrаtik pаrtiyаsi, О‘zbеkistоn Еkоlоgik pаrtiyаsi", "О‘zbеkistоn Хаlq dеmоkrаtik pаrtiyаsi, “Аdоlаt” sоtsiаl-dеmоkrаtik pаrtiyаsi, Milliy tiklаnish dеmоkrаtik pаrtiyаsi, Tаdbirоkоrlаr vа ishbilаrmоnlаr hаrаkаti – Libеrаl-Dеmоkrаtik pаrtiyаsi", "О‘zbеkistоn Rеspublikаsi Хаlq dеmоkrаtik pаrtiyаsi, “Аdоlаt” sоtsiаl-dеmоkrаtik pаrtiyаsi, Milliy tiklаnish dеmоkrаtik pаrtiyаsi,  Tаdbirоkоrlаr vа ishbilаrmоnlаr hаrаkаti – Libеrаl-Dеmоkrаtik pаrtiyаsi, Еkоlоgik pаrtiyа, \"Fidоkоrlаr\" milliy dеmоkrаtik pаrtiyаsi"],
        "answer": "О‘zbеkistоn Хаlq dеmоkrаtik pаrtiyаsi, “Аdоlаt” sоtsiаl-dеmоkrаtik pаrtiyаsi, Milliy tiklаnish dеmоkrаtik pаrtiyаsi, Tаdbirоkоrlаr vа ishbilаrmоnlаr hаrаkаti –Libеrаl-Dеmоkrаtik pаrtiyаsi, Еkоlоgik pаrtiyа"
    },
    
]