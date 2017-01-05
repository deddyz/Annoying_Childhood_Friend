
label start_prolog:

   #Prolog

    play sound opendoor_morning

    play sound walking_morning

    scene black
    
    "Aku perlahan membuka pintu rumahku,"

    "Jalanku cukup pelan menuju sekolah."

    play sound birds

    "Udara masih terasa dingin,"


    ## masukan CG disini
    show lisa_cg:

        #show from bottom
        xalign 0.0 yalign 1.0

        #move to top with 1.0 seconds
        linear 2.5 yalign 0.0

        #ease 1.0 truecenter

    
    "Namaku Lisa Angelic,"

    "Aku bisa terbilang populer karena kecantikanku"

    "dan karena gen dari orang tuaku yang berasal dari negara Inggris."

    "Bahkan beberapa lelaki pernah memintaku untuk menjadi kekasih mereka,"

    "tapi sayangnya aku menolak mereka,"

    "alasannya tentu saja karena aku sudah mempunyai lelaki yang aku suka."

    ## Masuk ke layar gelap dengan fade atas bawah.

    scene black with fade 

    "Udara terasa begitu segar di pagi hari."

    "aku beryukur bisa hidup sampai saat ini."

    ## masukan suara langkah kaki

    play sound walking_fast

    anonim "Maaf Lisa, aku tergelincir!!"

# # masukan suara orang didorong serta goyangkan layar.

    play sound hit_body

    with Shake((0, 0, 0, 0), 0.5, dist=15)

# # kembali ke scene normal.

    scene bg jalanan with fade

    play music prolog

    show ivan_senyum cropped with dissolve

    i "Maaf ya, maaf. Jalanannya licin."

    "Nada bicaranya yang seolah-olah meremehkanku,"

    l "Pembohong!"

    "Jika dia benar-benar tergelincir,"

    "tentu saja aku bisa memaafkannya."

    "Tapi nadanya itu!"

    "dia seakan-akan sengaja mendorongku hingga aku terjatuh seperti ini."

    l "Kamu hanya mengusiliku lagi, kan?!"

    i "Ahahahaha,"



    #suara pot jatuh

# # masukan clip gambar pot jatuh
    
    pause 1.0

    #PRANKK!!!

    show vas_bunga at vas_center with dissolve

    hide ivan_senyum cropped


    show ivan_kaget cropped behind vas_bunga at center, Shake(None, 1.0, dist=5)

    "Sebuah vas bunga jatuh tepat dari atas laki-laki yang mendorongku itu,"

    "tapi untung saja dia dapat menghindari vas bunga tersebut dengan cepat."

    hide vas_bunga at vas_center with dissolve

    hide ivan_kaget cropped

    #Ivan
    show ivan_marah cropped

    i "Ke-kenapa kamu malah tertawa!"

    #Lisa
    l "Ahahahahaha, rasakan itu Ivan!"

    l "Itu karma dari Tuhan karena telah usil kepadaku!"

    #Ivan
    i "I-itu tidak lucu!"

    i "Bagaimana kalau vas itu mengenai kepalaku!"

    #Lisa
    l "Entahlah,"

    l "mungkin kepalamu hanya akan bocor..."

    "aku tersenyum,"
    "kemudian aku bangun dan membersihkan rokku yang kotor."

    ## masukan suara tepukan kecil

    "Lelaki yang berada didepanku ini bernama Ivan,"
    "dia teman masa kecilku."
    "Entah sejak kapan"
    "Jalan pikirannya tidak pernah bisa kumengerti."
    "Dia benar-benar suka mengangguku dengan alasan yang tidak jelas seperti tadi."
    "Dia juga satu-satunya temanku kondisi tubuhku yang lemah."
    "Tapi meski dia mengetahui kondisi tubuhku ini,dia tetap bersikap seperti biasanya padaku,"
    "dia seakan-akan berpura-pura tidak tau tentang kondisiku ini."

    with fade

    #Ivan

    i "Apa kamu menginginkan kepalaku pecah?"

    #Lisa
    l "Mungkin saja. Jika---"

    #Arthur dengan label tanda tanya di awal

    anonim "Lisa! Ivan...!"

# # Hide Ivan

    hide ivan_marah cropped with dissolve


    "Seorang lelaki yang cukup jauh dibelakang kami berteriak memotong perkataanku."

# # Show Arthur dari jauh dulu. Berbarengan dengan Karin

    show arthur_normal small at my_left
    show karin small at my_right

    with fade

    pause 1.0


    hide arthur_normal samll at my_left
    hide karin small at my_right


# # Show ivan muka sebel
    show ivan_sebel cropped with dissolve

    "Aku sudah tau siapa yang berteriak,"
    "aku bisa tau orang tersebut hanya dengan mendengar suaranya saja."
    "Alasannya tentu saja karena aku sangat menyukai lelaki tersebut."

    hide ivan_sebel cropped

# # Show Arthur mendekat. Posisi middle antara Ivan dan Karin.

    with fade
    
    show arthur_normal cropped at center


    "Arthur Ryuuki, lelaki  yang sangat populer disekolahku."
    "Dari penampilannya sudah dapat dipastikan kalau dia keturunan dari benua berbeda,"
    "yakni Eropa dan Asia."
    "Selain tampan dia benar-benar baik dan sangat perhatian terhadap orang lain."


    hide arthur_normal cropped at center 

    with dissolve

    show ivan_sebel cropped with dissolve


    i "Ohh ohhhh, datang mas populer,"

    "Ya, tentu saja sifat Arthur sangat berkebalikan dengan teman masa kecilku ini."

    "Ivan terkadang memasang wajah yang menyebalkan saat Arthur datang mendekatiku."
    "Tidak hanya itu saja,"
    "dia bahkan pernah memukul beberapa lelaki yang hampir berpacaran denganku."
    "Aku benar-benar tidak mengerti apa yang dia pikirkan saat itu,"
    "kenapa dia selalu menghalangi kebahagiaanku?!"


    hide ivan_sebel cropped

    show ivan_tablo cropped


    l "Awas jika kamu membuat masalah lagi!"

    "aku tidak ingin Ivan menghancurkan jalan cintaku kali ini."

    hide ivan_tablo cropped

    show ivan_sebel cropped

    i "Berisik, ayo kita pergi! Kita hampir terlam---"

    l "Apa yang kamu katakan?! Kita harus menunggu Art----"

# # hide Arthur dan Ivan lalu show Karin
    
    #hide arthur_normal cropped at center

    #hide ivan_sebel cropped at posisi_kiri

    #hide karin cropped at posisi_kanan


    hide ivan_sebel cropped with dissolve

    #Karin
    show karin cropped

    with fade

    k "Ivan!!"

# # hide lalu show Ivan muka ngeledek


    "Aku tidak menyadari keberadaan gadis tersebut."
    "Saat Arthur berteriak, aku hanya fokus memperhatikannya,"
    "tidak melirik yang lainnya."

# # show Ivan muka ngeledek

    hide karin cropped with dissolve

    show ivan_ngeledek cropped with dissolve

    i "Ciee, rivalnya datang"

    "Aku membalas Ivan dengan lirikan sinis."
    "Wajahnya benar-benar membuatku kesal,"
    "Dia terlihat bahagia saat aku terbakar cemburu seperti ini."

# # show Ivan muka senyum


    hide ivan_ngeledek cropped

    show ivan_senyum cropped

    i "Yooo Karin!!"


# # hide Ivan lalu show Karin

    hide ivan_senyum cropped

    show karin cropped

    k "..."

    "Karin Viona,"
    "gadis cantik keturunan Rusia ini merupakan rivalku."
    "Bukan rival karena kepopuleran di sekolah, tetapi karena Arthur."
    "Aku tidak tau perasaanya pada Arthur, tapi dia benar-benar sangat dekat dengan Arthur."
    "Mereka bagaikan seperti sepasang kekasih bagiku."

    hide karin cropped

    #show ivan
    show ivan_senyum cropped


    hide ivan_senyum cropped
    with dissolve

    show arthur_segan2 cropped
    with fade


    a "Maaf membuat kalian menunggu,"


    hide arthur_segan2 cropped
    with fade

    #logic position

    #show arthur_normal cropped at my_left

    #show karin at my_right

    #with dissolve

    #hide arthur_normal cropped at my_left

    #hide karin cropped at my_right

    #with fade


# # show ivan marah

    show ivan_marah cropped

    i "Memang benar kamu membuat kami menunggu! Apa tidak bisa lebih cepa---"

    hide ivan_marah cropped

    show ivan_kaget cropped at center, Shake(None, 1.0, dist=5)

# # masukan suara injakan lalu goyangkan Ivan

    l "Ti-tidak apa kok, berangkat bersama-sama kan lebih seru!"

    "senyumku sambil menginjak kaki Ivan,"

    "aku menginjak kakinya sekuat tenagaku hingga dia memasang wajah yang kesakitan."

    hide ivan_kaget cropped

# # show ivan muka marah

    show ivan_marah cropped

    i "Sa-sakit! Apa yang kamu---"

# # show Ivan muka kesel
    hide ivan_marah cropped

    show ivan_kaget cropped

    l "Ayo kita berangkat!"

   
    hide ivan_kaget cropped

    show ivan_kesel cropped


    "Kembali lagi perkataan Ivan terpotong olehku"


    "Aku langsung menarik lengan Arthur."

    hide ivan_kesel cropped

    with fade

    show karin_kesel cropped with dissolve

# # show karin di samping Ivan, Ivan geser samping


    "Untuk sekilas, kulihat tatapan yang tidak mengenakan dari Karin saat aku menarik tangan Arthur."

    "Dia benar-benar menatapaku dengan tatapan yang seolah-olah sedang menahan amarahnya."

    "Tapi aku tidak takut dengan tatapanya!"

    "Aku akan membuat Arthur menjadi milikku."


    hide karin_kesel cropped at my_left

    hide ivan_kesel cropped at my_right

    with fade

# # show bg tanpa karakter

    play sound walking_morning

    "Kami berjalan ke sekolah secara berpasangan."

    "Aku dengan Arthur,"

    "Karin dengan Ivan."

    "Tekanan udara menjadi semakin berat saat itu."

    "Aku menolehkan kepalaku ke belakang,"

    "aku ingin melihat suasana disekitar Ivan dan Karin."

    with fade

    show ivan_kesel cropped at my_left

    show karin_kesel cropped at my_right

    with dissolve

# # show Ivan muka kesel dan Karin muka dingin

    "Terlihat tatapan yang tajam dari mereka berdua ke arahku."

    "Ok, aku bisa mengerti alasan Karin menatap tajam diriku."

    "tapi kenapa Ivan juga menatapku seperti itu?"

    "“Apa dia cemburu padaku?! Apa dia menyukaiku?”"

    "Ahahaha,"

    "anggapan tersebut merupakan anggapan terakhir yang aku berikan pada Ivan."

    "Dia mustahil menyukai gadis yang selalu ia ganggu,"

    "gadis sepertiku hanya ia anggap sebagai mainan untuk leluconnya."



    "Satu-satunya yang terpikirkan olehku adalah."

    "Dia ingin menggagalkan jalan cintaku lagi?"

    "Sebenarnya seberapa mengesalkannya anak ini!"

    "Kenapa dia sangat senang melihatku menderita?!”"

    "Aku harus bergerak cepat,"

    "banyak orang yang menghalangi jalan cintaku kali ini."


    hide ivan_kesel cropped at left

    hide karin_kesel cropped at right

    with fade

    "Pulang sekolah nanti aku harus mengatakannya,"

    "aku harus mengatakan"

    "kalau aku menyukai Arthur."

    #end of prolog

    jump chapter_1