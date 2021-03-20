<?php
        header('Access-Control-Allow-Origin');


        $data = [
            [
                'image' => 'https://s2.glbimg.com/D7J6124tRL_TBlcUZu89-UCeN0A=/0x0:3000x2000/1008x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/A/q/jZSLeyRaiUaM1bUSPavA/30b3cb85ec748c39a98aa65395f73302.kk111-dlk2206-0.jpg',
                'conteudo' => 'Fotografia de rua: Disinfection, funcionário desinfeta plataforma de trem em Ancara, Turquia — Foto: F. Dilek Uyar (Turquia)/Sony World Photography Awards'
            ],

            [
                'image' => 'https://s2.glbimg.com/alC-dCNdB-WKHsYn0Eu-m4Hc3jU=/0x0:4500x3000/1008x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/I/q/tpG5ZxSZ6lkkkyVkuyDA/78846a1a0ea99724dfcd49ec1fe67607.p1230533final-0.jpg',
                'conteudo' => 'Arquitetura: The Blue Window, vista de uma escada no hotel Hyatt de Düsseldorf, na Alemanha — Foto: Klaus Lenzen (Alemanha)/Sony World Photography Awards'
            ],

            [
                'image' => 'https://s2.glbimg.com/tporrS4NfSfjZ87VcaQNcK7DQOQ=/0x0:4480x6720/1008x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/0/S/wW4oXGSmC0dIgsXmDtNQ/2c68ebbc55bea3117be65d82242987e8.africanvictoriansubmit.jpg',
                'conteudo' => 'retrato de uma jovem negra com vestido vitoriano segurando utensílios tradicionais Shona — Foto: Tamary Kudita (Zimbábue)/Sony World Photography Awards'
            
            ]
        ];


    die(json_encode($data));

?>
