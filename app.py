from __future__ import annotations

from html import escape

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Korean Service Phrase Coach",
    page_icon="KR",
    layout="wide",
    initial_sidebar_state="expanded",
)


PHRASES = [
    {
        "id": "restaurant_table_two",
        "category": "Restaurants",
        "level": "Starter",
        "english": "Table for two, please.",
        "korean": "두 명 자리 부탁드려요.",
        "romanization": "Du myeong jari butakdeuryeoyo.",
        "slow": "두 명 / 자리 / 부탁드려요",
        "context": "Use this when arriving at a restaurant without a reservation.",
        "pronunciation": [
            "두 명 sounds like du myuhng. Keep 명 short and soft.",
            "자리 means seat or table in this context.",
            "부탁드려요 is a polite, service-friendly way to say please.",
        ],
        "response": "네, 이쪽으로 오세요. = Yes, please come this way.",
        "words": [
            ("두", "du", "two", "Native Korean number used before counters."),
            ("명", "myeong", "people", "Counter for people."),
            ("자리", "jari", "seat / table", "Literally seat or place."),
            ("부탁드려요", "butakdeuryeoyo", "please / I request", "Very polite and natural with service workers."),
        ],
    },
    {
        "id": "restaurant_reservation",
        "category": "Restaurants",
        "level": "Starter",
        "english": "I have a reservation.",
        "korean": "예약했어요.",
        "romanization": "Yeyakhaesseoyo.",
        "slow": "예약 / 했어요",
        "context": "Say this to the host when you arrive for a booked table.",
        "pronunciation": [
            "예 sounds like ye, not yay.",
            "약 is a quick yak sound.",
            "했어요 contracts naturally into hae-sseo-yo.",
        ],
        "response": "성함이 어떻게 되세요? = What name is it under?",
        "words": [
            ("예약", "yeyak", "reservation", "Also means booking or appointment."),
            ("했어요", "haesseoyo", "did / made", "Past polite form of 하다, to do."),
        ],
    },
    {
        "id": "restaurant_recommendation",
        "category": "Restaurants",
        "level": "Starter",
        "english": "What do you recommend?",
        "korean": "뭐가 제일 맛있어요?",
        "romanization": "Mwoga jeil masisseoyo?",
        "slow": "뭐가 / 제일 / 맛있어요",
        "context": "Useful when you want a server's recommendation.",
        "pronunciation": [
            "뭐가 sounds like mwo-ga.",
            "제일 means most or best.",
            "맛있어요 is usually pronounced ma-si-sseo-yo.",
        ],
        "response": "이 메뉴가 제일 잘 나가요. = This menu item is the most popular.",
        "words": [
            ("뭐가", "mwoga", "what", "뭐 plus subject marker 가."),
            ("제일", "jeil", "the most", "Used for superlatives like best or most."),
            ("맛있어요", "masisseoyo", "is delicious", "Polite present form."),
        ],
    },
    {
        "id": "restaurant_not_spicy",
        "category": "Restaurants",
        "level": "Starter",
        "english": "Please make it not spicy.",
        "korean": "안 맵게 해 주세요.",
        "romanization": "An maepge hae juseyo.",
        "slow": "안 / 맵게 / 해 주세요",
        "context": "Use when ordering food if you prefer mild flavors.",
        "pronunciation": [
            "안 is a clean ahn sound.",
            "맵게 sounds close to maep-geh.",
            "해 주세요 is the standard polite request ending.",
        ],
        "response": "네, 안 맵게 해 드릴게요. = Yes, we will make it not spicy.",
        "words": [
            ("안", "an", "not", "Negates the following description or action."),
            ("맵게", "maepge", "spicily", "From 맵다, to be spicy."),
            ("해 주세요", "hae juseyo", "please do / make", "A versatile polite request."),
        ],
    },
    {
        "id": "restaurant_no_meat",
        "category": "Restaurants",
        "level": "Travel Ready",
        "english": "Does this have meat in it?",
        "korean": "이거 고기 들어가요?",
        "romanization": "Igeo gogi deureogayo?",
        "slow": "이거 / 고기 / 들어가요",
        "context": "Use for dietary checks before ordering.",
        "pronunciation": [
            "이거 is ee-guh.",
            "고기 is go-gi, with both syllables short.",
            "들어가요 means goes in, used naturally for ingredients.",
        ],
        "response": "네, 돼지고기가 들어가요. = Yes, it has pork in it.",
        "words": [
            ("이거", "igeo", "this", "Casual but acceptable when pointing at a menu item."),
            ("고기", "gogi", "meat", "General word for meat."),
            ("들어가요", "deureogayo", "goes in / contains", "Common for asking about ingredients."),
        ],
    },
    {
        "id": "restaurant_water",
        "category": "Restaurants",
        "level": "Starter",
        "english": "Could we have some water, please?",
        "korean": "물 좀 주세요.",
        "romanization": "Mul jom juseyo.",
        "slow": "물 / 좀 / 주세요",
        "context": "A simple request at a restaurant or cafe.",
        "pronunciation": [
            "물 ends with the tongue lightly touching the roof of the mouth.",
            "좀 softens the request, like some or a bit.",
            "주세요 is ju-se-yo.",
        ],
        "response": "네, 가져다드릴게요. = Yes, I will bring it to you.",
        "words": [
            ("물", "mul", "water", "Often self-serve in casual restaurants."),
            ("좀", "jom", "some / please", "Makes requests sound softer."),
            ("주세요", "juseyo", "please give", "Essential polite request phrase."),
        ],
    },
    {
        "id": "restaurant_bill",
        "category": "Restaurants",
        "level": "Starter",
        "english": "Check, please.",
        "korean": "계산서 주세요.",
        "romanization": "Gyesanseo juseyo.",
        "slow": "계산서 / 주세요",
        "context": "Use at restaurants, though many Korean restaurants ask you to pay at the counter.",
        "pronunciation": [
            "계 sounds like gye, one syllable.",
            "계산서 means bill or check.",
            "주세요 keeps the sentence polite and simple.",
        ],
        "response": "카운터에서 계산하시면 돼요. = You can pay at the counter.",
        "words": [
            ("계산서", "gyesanseo", "bill / check", "The written check."),
            ("주세요", "juseyo", "please give", "Polite request."),
        ],
    },
    {
        "id": "restaurant_card",
        "category": "Payments",
        "level": "Starter",
        "english": "Can I pay by card?",
        "korean": "카드로 계산할 수 있어요?",
        "romanization": "Kadeuro gyesanhal su isseoyo?",
        "slow": "카드로 / 계산할 수 있어요",
        "context": "Useful before paying at restaurants, cafes, spas, and shops.",
        "pronunciation": [
            "카드로 is ka-deu-ro.",
            "계산할 means to pay or calculate.",
            "수 있어요 means can.",
        ],
        "response": "네, 카드 돼요. = Yes, card is okay.",
        "words": [
            ("카드로", "kadeuro", "by card", "로 means by or with."),
            ("계산할", "gyesanhal", "to pay", "From 계산하다."),
            ("수 있어요", "su isseoyo", "can", "Ability phrase."),
        ],
    },
    {
        "id": "spa_reservation",
        "category": "Spas",
        "level": "Starter",
        "english": "I have a reservation for a massage.",
        "korean": "마사지 예약했어요.",
        "romanization": "Masaji yeyakhaesseoyo.",
        "slow": "마사지 / 예약했어요",
        "context": "Use when checking in at a spa or massage clinic.",
        "pronunciation": [
            "마사지 sounds like ma-sa-ji.",
            "예약했어요 means made a reservation.",
            "Keep the final 요 gentle, not exaggerated.",
        ],
        "response": "예약자 성함이 어떻게 되세요? = What name is the reservation under?",
        "words": [
            ("마사지", "masaji", "massage", "Loanword from English."),
            ("예약했어요", "yeyakhaesseoyo", "made a reservation", "Polite past tense."),
        ],
    },
    {
        "id": "spa_pressure",
        "category": "Spas",
        "level": "Travel Ready",
        "english": "A little softer, please.",
        "korean": "조금 약하게 해 주세요.",
        "romanization": "Jogeum yakage hae juseyo.",
        "slow": "조금 / 약하게 / 해 주세요",
        "context": "Use during a massage when the pressure is too strong.",
        "pronunciation": [
            "조금 means a little and sounds like jo-geum.",
            "약하게 means softly or gently.",
            "해 주세요 turns it into a polite request.",
        ],
        "response": "네, 괜찮으세요? = Yes, are you okay?",
        "words": [
            ("조금", "jogeum", "a little", "Useful in many service situations."),
            ("약하게", "yakage", "softly / gently", "From 약하다, to be weak or gentle."),
            ("해 주세요", "hae juseyo", "please do / make", "Polite request."),
        ],
    },
    {
        "id": "spa_stronger",
        "category": "Spas",
        "level": "Travel Ready",
        "english": "A little stronger, please.",
        "korean": "조금 세게 해 주세요.",
        "romanization": "Jogeum sege hae juseyo.",
        "slow": "조금 / 세게 / 해 주세요",
        "context": "Use during a massage when you want more pressure.",
        "pronunciation": [
            "세게 sounds like seh-geh.",
            "The phrase structure mirrors the softer request.",
            "Use a friendly tone because this is a direct adjustment.",
        ],
        "response": "네, 이렇게 괜찮으세요? = Yes, is this okay?",
        "words": [
            ("조금", "jogeum", "a little", "Softens the request."),
            ("세게", "sege", "strongly", "From 세다, to be strong."),
            ("해 주세요", "hae juseyo", "please do / make", "Polite request."),
        ],
    },
    {
        "id": "spa_hurts",
        "category": "Spas",
        "level": "Travel Ready",
        "english": "It hurts a little.",
        "korean": "조금 아파요.",
        "romanization": "Jogeum apayo.",
        "slow": "조금 / 아파요",
        "context": "Use at a spa, clinic, or salon when something is uncomfortable.",
        "pronunciation": [
            "아파요 is ah-pa-yo.",
            "조금 makes it sound less abrupt.",
            "Raise your tone slightly if you want it to sound like a gentle alert.",
        ],
        "response": "아, 죄송합니다. = Oh, I am sorry.",
        "words": [
            ("조금", "jogeum", "a little", "A helpful softener."),
            ("아파요", "apayo", "it hurts", "Polite present form."),
        ],
    },
    {
        "id": "spa_finished",
        "category": "Spas",
        "level": "Starter",
        "english": "Thank you. It was very nice.",
        "korean": "감사합니다. 정말 좋았어요.",
        "romanization": "Gamsahamnida. Jeongmal joasseoyo.",
        "slow": "감사합니다 / 정말 / 좋았어요",
        "context": "A warm phrase for leaving a spa, restaurant, hotel, or salon.",
        "pronunciation": [
            "감사합니다 is formal and respectful.",
            "정말 means really.",
            "좋았어요 sounds like jo-a-sseo-yo.",
        ],
        "response": "감사합니다. 또 오세요. = Thank you. Please come again.",
        "words": [
            ("감사합니다", "gamsahamnida", "thank you", "Formal and safe anywhere."),
            ("정말", "jeongmal", "really", "Adds warmth or emphasis."),
            ("좋았어요", "joasseoyo", "was good / nice", "Polite past tense."),
        ],
    },
    {
        "id": "general_excuse",
        "category": "General Service",
        "level": "Starter",
        "english": "Excuse me.",
        "korean": "저기요.",
        "romanization": "Jeogiyo.",
        "slow": "저기요",
        "context": "Use to politely get a service worker's attention.",
        "pronunciation": [
            "저 sounds like juh, not joe.",
            "Keep it light and friendly.",
            "Avoid shouting; raise your hand slightly if needed.",
        ],
        "response": "네? = Yes?",
        "words": [
            ("저기요", "jeogiyo", "excuse me", "Common attention-getter in restaurants and shops."),
        ],
    },
    {
        "id": "general_sorry_korean",
        "category": "General Service",
        "level": "Starter",
        "english": "Sorry, I only speak a little Korean.",
        "korean": "죄송해요. 한국어 조금밖에 못해요.",
        "romanization": "Joesonghaeyo. Hangugeo jogeumbakke motaeyo.",
        "slow": "죄송해요 / 한국어 / 조금밖에 / 못해요",
        "context": "Use when a conversation moves too fast.",
        "pronunciation": [
            "죄송해요 is polite and slightly softer than the formal 죄송합니다.",
            "한국어 means Korean language.",
            "조금밖에 못해요 means can only do a little.",
        ],
        "response": "괜찮아요. = It is okay.",
        "words": [
            ("죄송해요", "joesonghaeyo", "sorry", "Polite apology."),
            ("한국어", "hangugeo", "Korean language", "한국 means Korea; 어 means language."),
            ("조금밖에", "jogeumbakke", "only a little", "밖에 pairs with a negative verb."),
            ("못해요", "motaeyo", "cannot do / speak well", "못 means cannot."),
        ],
    },
    {
        "id": "general_repeat",
        "category": "General Service",
        "level": "Starter",
        "english": "Could you say that again slowly?",
        "korean": "천천히 다시 말씀해 주세요.",
        "romanization": "Cheoncheonhi dasi malsseumhae juseyo.",
        "slow": "천천히 / 다시 / 말씀해 주세요",
        "context": "Use when you understood part of a sentence but need another try.",
        "pronunciation": [
            "천천히 means slowly.",
            "다시 means again.",
            "말씀해 주세요 is the respectful version of please say.",
        ],
        "response": "네, 천천히 말씀드릴게요. = Yes, I will say it slowly.",
        "words": [
            ("천천히", "cheoncheonhi", "slowly", "Useful in any conversation."),
            ("다시", "dasi", "again", "Also means once more."),
            ("말씀해 주세요", "malsseumhae juseyo", "please say", "Respectful speech for speaking."),
        ],
    },
    {
        "id": "transport_taxi_call",
        "category": "Transportation",
        "level": "Starter",
        "english": "Please call a taxi.",
        "korean": "택시 불러 주세요.",
        "romanization": "Taeksi bulleo juseyo.",
        "slow": "택시 / 불러 / 주세요",
        "context": "Use this when you need help getting a taxi from a hotel, restaurant, or spa.",
        "pronunciation": [
            "택시 is the English loanword taxi.",
            "불러 sounds like bul-luh, with a light double l sound.",
            "주세요 keeps the request polite.",
        ],
        "response": "네, 바로 불러 드릴게요. = Yes, I will call one right away.",
        "words": [
            ("택시", "taeksi", "taxi", "Loanword for a taxi."),
            ("불러", "bulleo", "call / summon", "From 부르다, to call."),
            ("주세요", "juseyo", "please do", "Polite request ending."),
        ],
    },
    {
        "id": "transport_address",
        "category": "Transportation",
        "level": "Starter",
        "english": "Please go to this address.",
        "korean": "이 주소로 가 주세요.",
        "romanization": "I jusoro ga juseyo.",
        "slow": "이 / 주소로 / 가 주세요",
        "context": "Use this with a taxi driver while showing the destination on your phone.",
        "pronunciation": [
            "이 is a short ee sound meaning this.",
            "주소 is ju-so, meaning address.",
            "가 주세요 means please go.",
        ],
        "response": "네, 알겠습니다. = Yes, understood.",
        "words": [
            ("이", "i", "this", "Points to the address you are showing."),
            ("주소로", "jusoro", "to the address", "로 marks the destination or direction."),
            ("가 주세요", "ga juseyo", "please go", "Polite request to go somewhere."),
        ],
    },
    {
        "id": "transport_subway_station",
        "category": "Transportation",
        "level": "Starter",
        "english": "Where is the subway station?",
        "korean": "지하철역이 어디예요?",
        "romanization": "Jihacheolyeogi eodiyeyo?",
        "slow": "지하철역이 / 어디예요",
        "context": "Use this when looking for the nearest subway entrance.",
        "pronunciation": [
            "지하철 sounds like ji-ha-chul.",
            "역 is yeok, meaning station.",
            "어디예요 means where is it?",
        ],
        "response": "저쪽에 있어요. = It is over there.",
        "words": [
            ("지하철역이", "jihacheoryeogi", "subway station", "이 marks the station as the subject."),
            ("어디예요", "eodiyeyo", "where is it?", "Polite question asking for a location."),
        ],
    },
    {
        "id": "transport_subway_exit",
        "category": "Transportation",
        "level": "Travel Ready",
        "english": "Which exit should I use?",
        "korean": "몇 번 출구로 나가야 해요?",
        "romanization": "Myeot beon chulguro nagaya haeyo?",
        "slow": "몇 번 / 출구로 / 나가야 해요",
        "context": "Useful in large subway stations with many exits.",
        "pronunciation": [
            "몇 번 sounds like myut bun.",
            "출구 is chul-gu, meaning exit.",
            "나가야 해요 means have to go out or should leave.",
        ],
        "response": "3번 출구로 나가세요. = Go out through exit 3.",
        "words": [
            ("몇 번", "myeot beon", "which number", "Asks which numbered option."),
            ("출구로", "chulguro", "through the exit", "로 marks the route or direction."),
            ("나가야 해요", "nagaya haeyo", "should go out", "Expresses what you need to do."),
        ],
    },
    {
        "id": "transport_airport",
        "category": "Transportation",
        "level": "Travel Ready",
        "english": "How do I get to the airport?",
        "korean": "공항에 가려면 어떻게 가요?",
        "romanization": "Gonghange garyeomyeon eotteoke gayo?",
        "slow": "공항에 / 가려면 / 어떻게 가요",
        "context": "Use this when asking for the best route to the airport.",
        "pronunciation": [
            "공항 is gong-hang, meaning airport.",
            "가려면 means if I want to go or to get to.",
            "어떻게 가요 means how do I go?",
        ],
        "response": "공항철도를 타세요. = Take the Airport Railroad.",
        "words": [
            ("공항에", "gonghange", "to the airport", "에 marks the destination."),
            ("가려면", "garyeomyeon", "to get to / if going", "Conditional form of 가다, to go."),
            ("어떻게 가요", "eotteoke gayo", "how do I go?", "Asks for directions or a route."),
        ],
    },
    {
        "id": "transport_bus_destination",
        "category": "Transportation",
        "level": "Travel Ready",
        "english": "Does this bus go to Myeongdong?",
        "korean": "이 버스가 명동에 가요?",
        "romanization": "I beoseuga Myeongdong-e gayo?",
        "slow": "이 버스가 / 명동에 / 가요",
        "context": "Replace 명동 with any destination when checking a bus route.",
        "pronunciation": [
            "버스 is beoh-suh, the Korean word for bus.",
            "명동 is Myeong-dong, a well-known Seoul shopping area.",
            "가요 is the polite form of go.",
        ],
        "response": "네, 가요. = Yes, it goes there.",
        "words": [
            ("이 버스가", "i beoseuga", "this bus", "이 means this and 가 marks the subject."),
            ("명동에", "Myeongdong-e", "to Myeongdong", "에 marks the destination."),
            ("가요", "gayo", "goes", "Polite present form of 가다."),
        ],
    },
    {
        "id": "hotel_check_in",
        "category": "Accommodation",
        "level": "Starter",
        "english": "I would like to check in.",
        "korean": "체크인하고 싶어요.",
        "romanization": "Chekeu-inhago sipeoyo.",
        "slow": "체크인하고 / 싶어요",
        "context": "Use this when arriving at a hotel or guesthouse.",
        "pronunciation": [
            "체크인 is the loanword check-in.",
            "하고 connects the action to 싶어요.",
            "싶어요 means would like to or want to.",
        ],
        "response": "체크인 도와드릴게요. = I will help you check in.",
        "words": [
            ("체크인하고", "chekeu-inhago", "check in and", "Uses the English loanword with 하고."),
            ("싶어요", "sipeoyo", "would like to", "Polite form expressing a wish."),
        ],
    },
    {
        "id": "hotel_wifi_password",
        "category": "Accommodation",
        "level": "Starter",
        "english": "What is the Wi-Fi password?",
        "korean": "와이파이 비밀번호가 뭐예요?",
        "romanization": "Waipai bimilbeonhoga mwoyeyo?",
        "slow": "와이파이 / 비밀번호가 / 뭐예요",
        "context": "Ask this at a hotel, café, spa, or other guest service desk.",
        "pronunciation": [
            "와이파이 is the loanword Wi-Fi.",
            "비밀번호 sounds like bee-mil-bun-ho.",
            "뭐예요 means what is it?",
        ],
        "response": "여기 적혀 있어요. = It is written here.",
        "words": [
            ("와이파이", "waipai", "Wi-Fi", "Loanword for wireless internet."),
            ("비밀번호가", "bimilbeonhoga", "password", "이 marks the password as the subject."),
            ("뭐예요", "mwoyeyo", "what is it?", "Polite question asking for information."),
        ],
    },
    {
        "id": "hotel_luggage_storage",
        "category": "Accommodation",
        "level": "Travel Ready",
        "english": "Can I leave my luggage here?",
        "korean": "짐을 맡길 수 있어요?",
        "romanization": "Jimeul matgil su isseoyo?",
        "slow": "짐을 / 맡길 수 있어요",
        "context": "Use this before check-in or after checkout when you want hotel staff to hold your bags.",
        "pronunciation": [
            "짐 means luggage or belongings.",
            "맡길 sounds like mat-gil, with a short final l.",
            "수 있어요 means can or is it possible?",
        ],
        "response": "네, 맡아 드릴게요. = Yes, we can hold it for you.",
        "words": [
            ("짐을", "jimeul", "luggage", "을 marks the luggage as the object."),
            ("맡길", "matgil", "to leave in someone’s care", "From 맡기다, to entrust or store."),
            ("수 있어요", "su isseoyo", "can", "Ability or possibility expression."),
        ],
    },
    {
        "id": "hotel_extra_towel",
        "category": "Accommodation",
        "level": "Starter",
        "english": "Please give me one more towel.",
        "korean": "수건 하나 더 주세요.",
        "romanization": "Sugeon hana deo juseyo.",
        "slow": "수건 / 하나 더 / 주세요",
        "context": "Use this when requesting another towel at a hotel, spa, or sauna.",
        "pronunciation": [
            "수건 sounds like soo-guhn.",
            "하나 means one.",
            "더 means more or one additional item.",
        ],
        "response": "네, 가져다드릴게요. = Yes, I will bring it to you.",
        "words": [
            ("수건", "sugeon", "towel", "The everyday word for towel."),
            ("하나 더", "hana deo", "one more", "하나 is one and 더 means more."),
            ("주세요", "juseyo", "please give", "Polite request phrase."),
        ],
    },
    {
        "id": "hotel_checkout_time",
        "category": "Accommodation",
        "level": "Starter",
        "english": "What time is checkout?",
        "korean": "체크아웃은 몇 시예요?",
        "romanization": "Chekeuauseun myeot siyeyo?",
        "slow": "체크아웃은 / 몇 시예요",
        "context": "Ask this at a hotel or guesthouse so you know when to leave.",
        "pronunciation": [
            "체크아웃 is the loanword checkout.",
            "은 marks the topic of the question.",
            "몇 시예요 means what time is it?",
        ],
        "response": "오전 열한 시예요. = It is 11 a.m.",
        "words": [
            ("체크아웃은", "chekeuauseun", "as for checkout", "Topic form of checkout."),
            ("몇 시예요", "myeot siyeyo", "what time is it?", "몇 means which/how many and 시 means hour."),
        ],
    },
    {
        "id": "hotel_room_problem",
        "category": "Accommodation",
        "level": "Travel Ready",
        "english": "There is a problem with my room.",
        "korean": "방에 문제가 있어요.",
        "romanization": "Bange munjega isseoyo.",
        "slow": "방에 / 문제가 / 있어요",
        "context": "Use this at the front desk when something in your room needs attention.",
        "pronunciation": [
            "방 is bang, meaning room.",
            "문제 means problem or issue.",
            "있어요 means there is or exists.",
        ],
        "response": "어떤 문제예요? = What is the problem?",
        "words": [
            ("방에", "bange", "in the room", "에 marks the location."),
            ("문제가", "munjega", "a problem", "이 marks the problem as the subject."),
            ("있어요", "isseoyo", "there is", "Polite form of 있다, to exist."),
        ],
    },
    {
        "id": "directions_restroom",
        "category": "Directions",
        "level": "Starter",
        "english": "Where is the restroom?",
        "korean": "화장실이 어디예요?",
        "romanization": "Hwajangsiri eodiyeyo?",
        "slow": "화장실이 / 어디예요",
        "context": "Useful in restaurants, cafés, stations, malls, and spas.",
        "pronunciation": [
            "화장실 sounds like hwa-jang-shil.",
            "실 is a short shil sound, not seal.",
            "어디예요 means where is it?",
        ],
        "response": "저쪽에 있어요. = It is over there.",
        "words": [
            ("화장실이", "hwajangsiri", "restroom", "이 marks the restroom as the subject."),
            ("어디예요", "eodiyeyo", "where is it?", "Polite location question."),
        ],
    },
    {
        "id": "directions_convenience_store",
        "category": "Directions",
        "level": "Starter",
        "english": "Is there a convenience store nearby?",
        "korean": "이 근처에 편의점이 있어요?",
        "romanization": "I geuncheoe pyeonuijeomi isseoyo?",
        "slow": "이 근처에 / 편의점이 / 있어요",
        "context": "Use this when you need snacks, drinks, toiletries, or a quick purchase.",
        "pronunciation": [
            "근처 sounds like geun-chuh, meaning nearby area.",
            "편의점 is pyeon-ui-jeom, a convenience store.",
            "있어요 asks whether something exists or is present.",
        ],
        "response": "네, 바로 앞에 있어요. = Yes, it is right in front.",
        "words": [
            ("이 근처에", "i geuncheoe", "near here", "에 marks the nearby area."),
            ("편의점이", "pyeonuijeomi", "convenience store", "이 marks the store as the subject."),
            ("있어요", "isseoyo", "there is", "Polite existence phrase."),
        ],
    },
    {
        "id": "directions_walking_time",
        "category": "Directions",
        "level": "Starter",
        "english": "How long does it take on foot?",
        "korean": "걸어서 얼마나 걸려요?",
        "romanization": "Georeoseo eolmana geollyeoyo?",
        "slow": "걸어서 / 얼마나 / 걸려요",
        "context": "Ask this before deciding whether a destination is walkable.",
        "pronunciation": [
            "걸어서 sounds like guh-ruh-suh.",
            "얼마나 means how much or how long.",
            "걸려요 means takes time.",
        ],
        "response": "십 분 정도 걸려요. = It takes about ten minutes.",
        "words": [
            ("걸어서", "georeoseo", "on foot", "Means by walking."),
            ("얼마나", "eolmana", "how much / how long", "Asks about amount or duration."),
            ("걸려요", "geollyeoyo", "takes time", "Polite form of 걸리다."),
        ],
    },
    {
        "id": "directions_lost",
        "category": "Directions",
        "level": "Starter",
        "english": "I am lost.",
        "korean": "길을 잃었어요.",
        "romanization": "Gireul ireosseoyo.",
        "slow": "길을 / 잃었어요",
        "context": "Use this when you need someone to help you find your way.",
        "pronunciation": [
            "길 is gil, meaning road or way.",
            "잃었어요 sounds like ee-ruh-suh-yo.",
            "The past form shows that you have become lost.",
        ],
        "response": "어디를 찾으세요? = What are you looking for?",
        "words": [
            ("길을", "gireul", "the way / road", "을 marks the road as the object."),
            ("잃었어요", "ireosseoyo", "lost", "Past polite form of 잃다, to lose."),
        ],
    },
    {
        "id": "directions_nearby",
        "category": "Directions",
        "level": "Starter",
        "english": "Is it close from here?",
        "korean": "여기에서 가까워요?",
        "romanization": "Yeogieseo gakkawoyo?",
        "slow": "여기에서 / 가까워요",
        "context": "Use this when deciding whether to walk or take transportation.",
        "pronunciation": [
            "여기에서 means from here.",
            "가까워요 sounds like ga-kka-wo-yo.",
            "The doubled ㄲ in 가까워요 is a firm k sound.",
        ],
        "response": "네, 걸어서 오 분이에요. = Yes, it is a five-minute walk.",
        "words": [
            ("여기에서", "yeogieseo", "from here", "에서 marks the starting point."),
            ("가까워요", "gakkawoyo", "is close", "Polite form of 가깝다, to be near."),
        ],
    },
    {
        "id": "shopping_price",
        "category": "Shopping",
        "level": "Starter",
        "english": "How much is this?",
        "korean": "이거 얼마예요?",
        "romanization": "Igeo eolmayeyo?",
        "slow": "이거 / 얼마예요",
        "context": "Use this in shops, markets, cafés, and souvenir stores.",
        "pronunciation": [
            "이거 sounds like ee-guh and means this.",
            "얼마예요 means how much is it?",
            "Keep the final 요 light and polite.",
        ],
        "response": "만 원이에요. = It is 10,000 won.",
        "words": [
            ("이거", "igeo", "this", "Points to the item you mean."),
            ("얼마예요", "eolmayeyo", "how much is it?", "Polite price question."),
        ],
    },
    {
        "id": "shopping_try_on",
        "category": "Shopping",
        "level": "Travel Ready",
        "english": "Can I try this on?",
        "korean": "입어 봐도 돼요?",
        "romanization": "Ibeo bwado dwaeyo?",
        "slow": "입어 봐도 / 돼요",
        "context": "Use this when shopping for clothing or shoes.",
        "pronunciation": [
            "입어 sounds like ee-buh.",
            "봐도 means even if I try or may I try.",
            "돼요 means is it okay?",
        ],
        "response": "네, 입어 보세요. = Yes, try it on.",
        "words": [
            ("입어", "ibeo", "wear / put on", "From 입다, to wear."),
            ("봐도", "bwado", "even if I try", "봐 means try doing something."),
            ("돼요", "dwaeyo", "is it okay?", "Polite permission expression."),
        ],
    },
    {
        "id": "shopping_larger_size",
        "category": "Shopping",
        "level": "Travel Ready",
        "english": "Do you have a larger size?",
        "korean": "더 큰 사이즈 있어요?",
        "romanization": "Deo keun saijeu isseoyo?",
        "slow": "더 큰 / 사이즈 / 있어요",
        "context": "Use this when a piece of clothing or shoe is too small.",
        "pronunciation": [
            "더 means more or another amount.",
            "큰 is keun, meaning big or large.",
            "사이즈 is the loanword size.",
        ],
        "response": "네, 이 사이즈가 더 커요. = Yes, this size is larger.",
        "words": [
            ("더 큰", "deo keun", "larger", "더 adds the meaning more."),
            ("사이즈", "saijeu", "size", "Loanword for size."),
            ("있어요", "isseoyo", "do you have?", "Asks whether it exists or is available."),
        ],
    },
    {
        "id": "shopping_different_color",
        "category": "Shopping",
        "level": "Starter",
        "english": "Do you have another color?",
        "korean": "다른 색 있어요?",
        "romanization": "Dareun saek isseoyo?",
        "slow": "다른 / 색 / 있어요",
        "context": "Use this when you like an item but want to see another color.",
        "pronunciation": [
            "다른 sounds like da-reun, meaning different or another.",
            "색 is saek, meaning color.",
            "있어요 can mean do you have? in a shop.",
        ],
        "response": "검은색도 있어요. = We also have black.",
        "words": [
            ("다른", "dareun", "another / different", "Describes a different option."),
            ("색", "saek", "color", "The general word for color."),
            ("있어요", "isseoyo", "do you have?", "Asks about availability."),
        ],
    },
    {
        "id": "shopping_tax_refund",
        "category": "Shopping",
        "level": "Travel Ready",
        "english": "Is a tax refund available?",
        "korean": "면세 환급 돼요?",
        "romanization": "Myeonse hwanggeup dwaeyo?",
        "slow": "면세 / 환급 / 돼요",
        "context": "Ask this at eligible shops before paying, and keep your passport handy.",
        "pronunciation": [
            "면세 sounds like myun-seh and relates to tax-free shopping.",
            "환급 is hwan-geup, meaning refund.",
            "돼요 asks whether it is possible or available.",
        ],
        "response": "네, 여권 보여 주세요. = Yes, please show your passport.",
        "words": [
            ("면세", "myeonse", "tax-free", "Used for tax exemption or duty-free shopping."),
            ("환급", "hwanggeup", "refund", "Money returned after a payment."),
            ("돼요", "dwaeyo", "is it possible?", "Polite possibility question."),
        ],
    },
    {
        "id": "cafe_eat_here",
        "category": "Cafés",
        "level": "Starter",
        "english": "I will eat here.",
        "korean": "여기서 먹을게요.",
        "romanization": "Yeogiseo meogeulgeyo.",
        "slow": "여기서 / 먹을게요",
        "context": "Use this when ordering food or a drink for here rather than to go.",
        "pronunciation": [
            "여기서 means here, at this place.",
            "먹을게요 sounds like muh-geul-geh-yo.",
            "-ㄹ게요 can sound like I will or I will do that.",
        ],
        "response": "네, 여기서 드세요. = Yes, please eat here.",
        "words": [
            ("여기서", "yeogiseo", "here", "에서 marks the place where an action happens."),
            ("먹을게요", "meogeulgeyo", "I will eat", "Polite intention form of 먹다."),
        ],
    },
    {
        "id": "cafe_takeout",
        "category": "Cafés",
        "level": "Starter",
        "english": "Is takeout available?",
        "korean": "테이크아웃 돼요?",
        "romanization": "Teikeuaut dwaeyo?",
        "slow": "테이크아웃 / 돼요",
        "context": "Use this in cafés, bakeries, and casual restaurants.",
        "pronunciation": [
            "테이크아웃 is the Korean pronunciation of takeout.",
            "돼요 sounds like dwae-yo.",
            "The short question is natural and easy to use.",
        ],
        "response": "네, 가능합니다. = Yes, that is possible.",
        "words": [
            ("테이크아웃", "teikeuaut", "takeout", "Loanword for food to go."),
            ("돼요", "dwaeyo", "is it possible?", "Polite possibility question."),
        ],
    },
    {
        "id": "cafe_iced_americano",
        "category": "Cafés",
        "level": "Starter",
        "english": "One iced Americano, please.",
        "korean": "아이스 아메리카노 하나 주세요.",
        "romanization": "Aiseu amerikano hana juseyo.",
        "slow": "아이스 아메리카노 / 하나 / 주세요",
        "context": "A useful café order in Korea; change the drink name and number as needed.",
        "pronunciation": [
            "아이스 is the loanword iced.",
            "아메리카노 sounds like a-me-ri-ka-no.",
            "하나 means one and 주세요 means please give me.",
        ],
        "response": "사이즈는 어떻게 드릴까요? = What size would you like?",
        "words": [
            ("아이스", "aiseu", "iced", "Loanword used for cold drinks."),
            ("아메리카노", "amerikano", "Americano", "Coffee drink loanword."),
            ("하나", "hana", "one", "Native Korean number used for items."),
            ("주세요", "juseyo", "please give me", "Polite ordering phrase."),
        ],
    },
    {
        "id": "cafe_water_free",
        "category": "Cafés",
        "level": "Starter",
        "english": "Is the water free?",
        "korean": "물은 무료예요?",
        "romanization": "Mureun muryoyeyo?",
        "slow": "물은 / 무료예요",
        "context": "Ask this at a café, restaurant, or food court before taking bottled water.",
        "pronunciation": [
            "물은 sounds like moo-reun.",
            "무료 means free of charge.",
            "예요 is the polite form of is.",
        ],
        "response": "네, 무료예요. = Yes, it is free.",
        "words": [
            ("물은", "mureun", "as for the water", "은 marks water as the topic."),
            ("무료예요", "muryoyeyo", "is free", "무료 means free and 예요 means is."),
        ],
    },
    {
        "id": "cafe_split_bill",
        "category": "Cafés",
        "level": "Travel Ready",
        "english": "Please split the bill.",
        "korean": "따로 계산해 주세요.",
        "romanization": "Ttaro gyesanhae juseyo.",
        "slow": "따로 / 계산해 / 주세요",
        "context": "Use this when a group wants to pay separately.",
        "pronunciation": [
            "따로 starts with a firm tt sound and means separately.",
            "계산해 means calculate or charge.",
            "해 주세요 makes a polite request.",
        ],
        "response": "네, 따로 계산해 드릴게요. = Yes, I will split the bill.",
        "words": [
            ("따로", "ttaro", "separately", "Shows that the payments should be separate."),
            ("계산해", "gyesanhae", "calculate / charge", "From 계산하다, to calculate or pay."),
            ("주세요", "juseyo", "please do", "Polite request ending."),
        ],
    },
    {
        "id": "emergency_pharmacy",
        "category": "Emergencies",
        "level": "Starter",
        "english": "Where is a pharmacy?",
        "korean": "약국이 어디예요?",
        "romanization": "Yakgugi eodiyeyo?",
        "slow": "약국이 / 어디예요",
        "context": "Use this when you need basic medicine or health supplies.",
        "pronunciation": [
            "약국 sounds like yak-gook.",
            "약 means medicine and 국 means place or institution here.",
            "어디예요 means where is it?",
        ],
        "response": "이 길로 쭉 가세요. = Go straight along this road.",
        "words": [
            ("약국이", "yakgugi", "pharmacy", "이 marks the pharmacy as the subject."),
            ("어디예요", "eodiyeyo", "where is it?", "Polite location question."),
        ],
    },
    {
        "id": "emergency_hospital",
        "category": "Emergencies",
        "level": "Travel Ready",
        "english": "Where is a hospital?",
        "korean": "병원이 어디예요?",
        "romanization": "Byeongwoni eodiyeyo?",
        "slow": "병원이 / 어디예요",
        "context": "Use this when you need medical care or want help finding a clinic or hospital.",
        "pronunciation": [
            "병원 sounds like byung-won.",
            "병 is a short byung sound, not bee-yung.",
            "병원이 어디예요 means where is the hospital?",
        ],
        "response": "택시 타고 가세요. = Take a taxi there.",
        "words": [
            ("병원이", "byeongwoni", "hospital", "이 marks the hospital as the subject."),
            ("어디예요", "eodiyeyo", "where is it?", "Polite location question."),
        ],
    },
    {
        "id": "emergency_help",
        "category": "Emergencies",
        "level": "Starter",
        "english": "Please help me.",
        "korean": "도와주세요.",
        "romanization": "Dowajuseyo.",
        "slow": "도와 / 주세요",
        "context": "Use this when you need immediate assistance from a nearby person or staff member.",
        "pronunciation": [
            "도와 sounds like do-wa.",
            "The phrase is direct but polite because of 주세요.",
            "Say it clearly and repeat it if you need urgent attention.",
        ],
        "response": "무슨 일이세요? = What happened?",
        "words": [
            ("도와", "dowa", "help", "From 돕다, to help."),
            ("주세요", "juseyo", "please", "Polite request ending."),
        ],
    },
    {
        "id": "emergency_unwell",
        "category": "Emergencies",
        "level": "Travel Ready",
        "english": "I do not feel well.",
        "korean": "몸이 안 좋아요.",
        "romanization": "Momi an joayo.",
        "slow": "몸이 / 안 좋아요",
        "context": "Use this to tell hotel, spa, restaurant, or medical staff that you feel unwell.",
        "pronunciation": [
            "몸이 sounds like mo-mi.",
            "안 means not and comes before the adjective.",
            "좋아요 means good, so 안 좋아요 means not good.",
        ],
        "response": "괜찮으세요? = Are you okay?",
        "words": [
            ("몸이", "momi", "my body / I", "Korean often uses body for how one feels."),
            ("안 좋아요", "an joayo", "is not well", "안 negates 좋아요, to be good."),
        ],
    },
    {
        "id": "emergency_lost_passport",
        "category": "Emergencies",
        "level": "Travel Ready",
        "english": "I lost my passport.",
        "korean": "여권을 잃어버렸어요.",
        "romanization": "Yeogwoneul ireobeoryeosseoyo.",
        "slow": "여권을 / 잃어버렸어요",
        "context": "Use this at a hotel, police station, or embassy when your passport is missing.",
        "pronunciation": [
            "여권 sounds like yuh-gwon, meaning passport.",
            "잃어버렸어요 sounds like ee-ruh-buh-ryuh-suh-yo.",
            "The phrase is polite past tense for I lost it.",
        ],
        "response": "경찰서에 가 보세요. = Please try going to the police station.",
        "words": [
            ("여권을", "yeogwoneul", "passport", "을 marks the passport as the object."),
            ("잃어버렸어요", "ireobeoryeosseoyo", "lost", "Polite past form meaning lost completely."),
        ],
    },
]


HANGUL_INITIALS = [
    "g",
    "kk",
    "n",
    "d",
    "tt",
    "r",
    "m",
    "b",
    "pp",
    "s",
    "ss",
    "",
    "j",
    "jj",
    "ch",
    "k",
    "t",
    "p",
    "h",
]
HANGUL_MEDIALS = [
    "a",
    "ae",
    "ya",
    "yae",
    "eo",
    "e",
    "yeo",
    "ye",
    "o",
    "wa",
    "wae",
    "oe",
    "yo",
    "u",
    "wo",
    "we",
    "wi",
    "yu",
    "eu",
    "ui",
    "i",
]
HANGUL_FINALS = [
    "",
    "k",
    "k",
    "k",
    "n",
    "n",
    "n",
    "t",
    "l",
    "k",
    "m",
    "l",
    "l",
    "l",
    "p",
    "p",
    "m",
    "p",
    "p",
    "t",
    "t",
    "ng",
    "t",
    "t",
    "k",
    "t",
    "p",
    "t",
]
ROMANIZATION_OVERRIDES = {
    "잃어버렸어요": "ireobeoryeosseoyo",
    "괜찮으세요": "gwaenchanh-euseyo",
    "말씀드릴게요": "malsseumdeurilgeyo",
    "가져다드릴게요": "gajyeodadeurilgeyo",
    "어떻게": "eotteoke",
    "감사합니다": "gamsahamnida",
    "죄송합니다": "joesonghamnida",
    "드릴까요": "deurilkkayo",
    "드릴게요": "deurilgeyo",
    "있어요": "isseoyo",
    "좋아요": "joayo",
    "합니다": "hamnida",
}


def romanize_korean(text: str) -> str:
    """Return a readable Revised-Romanization-style guide for Hangul text."""
    for korean, pronunciation in sorted(
        ROMANIZATION_OVERRIDES.items(), key=lambda item: len(item[0]), reverse=True
    ):
        text = text.replace(korean, pronunciation)

    romanized = []
    for character in text:
        codepoint = ord(character)
        if 0xAC00 <= codepoint <= 0xD7A3:
            syllable = codepoint - 0xAC00
            initial = syllable // 588
            medial = (syllable % 588) // 28
            final = syllable % 28
            romanized.append(
                HANGUL_INITIALS[initial]
                + HANGUL_MEDIALS[medial]
                + HANGUL_FINALS[final]
            )
        else:
            romanized.append(character)
    return "".join(romanized)


CONVERSATION_RESPONSES = {
    "restaurant_table_two": [
        ("네, 이쪽으로 오세요.", "Yes, please come this way."),
        ("몇 분이세요?", "How many people?"),
        ("창가 자리 괜찮으세요?", "Is a window seat okay?"),
    ],
    "restaurant_reservation": [
        ("성함이 어떻게 되세요?", "What name is it under?"),
        ("예약 확인해 드릴게요.", "I will check your reservation."),
        ("잠시만 기다려 주세요.", "Please wait a moment."),
    ],
    "restaurant_recommendation": [
        ("이 메뉴가 제일 잘 나가요.", "This menu item is the most popular."),
        ("오늘은 이게 맛있어요.", "This is delicious today."),
        ("매운 음식 괜찮으세요?", "Is spicy food okay?"),
    ],
    "restaurant_not_spicy": [
        ("네, 안 맵게 해 드릴게요.", "Yes, we will make it not spicy."),
        ("조금 매울 수 있어요.", "It may be a little spicy."),
        ("고추는 빼 드릴게요.", "We will leave out the chili peppers."),
    ],
    "restaurant_no_meat": [
        ("네, 돼지고기가 들어가요.", "Yes, it contains pork."),
        ("고기는 안 들어가요.", "It does not contain meat."),
        ("소고기가 들어가요.", "It contains beef."),
    ],
    "restaurant_water": [
        ("네, 가져다드릴게요.", "Yes, I will bring it to you."),
        ("물은 셀프예요.", "Water is self-service."),
        ("여기 물 있습니다.", "Here is some water."),
    ],
    "restaurant_bill": [
        ("카운터에서 계산하시면 돼요.", "You can pay at the counter."),
        ("네, 바로 가져다드릴게요.", "Yes, I will bring it right away."),
        ("같이 계산해 드릴까요?", "Shall I combine the bill?"),
    ],
    "restaurant_card": [
        ("네, 카드 돼요.", "Yes, card is okay."),
        ("죄송하지만 현금만 돼요.", "Sorry, cash only."),
        ("여기 꽂아 주세요.", "Please insert it here."),
    ],
    "spa_reservation": [
        ("예약자 성함이 어떻게 되세요?", "What name is the reservation under?"),
        ("확인해 드릴게요.", "I will check it for you."),
        ("탈의실은 이쪽이에요.", "The changing room is this way."),
    ],
    "spa_pressure": [
        ("네, 괜찮으세요?", "Yes, is this okay?"),
        ("조금 약하게 해 드릴게요.", "I will make it a little softer."),
        ("이 정도면 괜찮으세요?", "Is this level okay?"),
    ],
    "spa_stronger": [
        ("네, 이렇게 괜찮으세요?", "Yes, is this okay?"),
        ("조금 더 세게 해 드릴게요.", "I will make it a little stronger."),
        ("너무 세면 말씀해 주세요.", "Please tell me if it is too strong."),
    ],
    "spa_hurts": [
        ("아, 죄송합니다.", "Oh, I am sorry."),
        ("괜찮으세요?", "Are you okay?"),
        ("바로 약하게 해 드릴게요.", "I will make it gentler right away."),
    ],
    "spa_finished": [
        ("감사합니다. 또 오세요.", "Thank you. Please come again."),
        ("오늘 마사지 괜찮으셨어요?", "Was the massage okay today?"),
        ("조심히 들어가세요.", "Take care on your way home."),
    ],
    "general_excuse": [
        ("네?", "Yes? How can I help?"),
        ("무슨 일이세요?", "What is it?"),
        ("도와드릴까요?", "Can I help you?"),
    ],
    "general_sorry_korean": [
        ("괜찮아요.", "It is okay."),
        ("천천히 말씀드릴게요.", "I will speak slowly."),
        ("영어 하실 수 있는 분 불러 드릴까요?", "Shall I call someone who speaks English?"),
    ],
    "general_repeat": [
        ("네, 다시 말씀드릴게요.", "Yes, I will say it again."),
        ("천천히 말씀드릴게요.", "I will speak slowly."),
        ("어느 부분이 어려우세요?", "Which part is difficult?"),
    ],
    "transport_taxi_call": [
        ("네, 바로 불러 드릴게요.", "Yes, I will call one right away."),
        ("어디로 가세요?", "Where are you going?"),
        ("잠시만 기다려 주세요.", "Please wait a moment."),
    ],
    "transport_address": [
        ("네, 알겠습니다.", "Yes, understood."),
        ("이 주소 맞으세요?", "Is this the correct address?"),
        ("도착하면 말씀드릴게요.", "I will tell you when we arrive."),
    ],
    "transport_subway_station": [
        ("저쪽에 있어요.", "It is over there."),
        ("이 건물 지하로 내려가세요.", "Go down to the basement of this building."),
        ("5분 정도 걸려요.", "It takes about five minutes."),
    ],
    "transport_subway_exit": [
        ("3번 출구로 나가세요.", "Go out through exit 3."),
        ("반대편 출구예요.", "It is the exit on the other side."),
        ("표지판을 따라가세요.", "Follow the signs."),
    ],
    "transport_airport": [
        ("공항철도를 타세요.", "Take the Airport Railroad."),
        ("택시가 제일 편해요.", "A taxi is the most convenient."),
        ("버스로 한 시간 정도 걸려요.", "It takes about an hour by bus."),
    ],
    "transport_bus_destination": [
        ("네, 가요.", "Yes, it goes there."),
        ("아니요, 다른 버스를 타세요.", "No, take another bus."),
        ("다음 정류장에서 내리세요.", "Get off at the next stop."),
    ],
    "hotel_check_in": [
        ("체크인 도와드릴게요.", "I will help you check in."),
        ("여권 보여 주세요.", "Please show your passport."),
        ("체크인은 오후 세 시부터예요.", "Check-in starts at 3 p.m."),
    ],
    "hotel_wifi_password": [
        ("여기 적혀 있어요.", "It is written here."),
        ("객실 안내에 있어요.", "It is in the room information."),
        ("와이파이는 무료예요.", "Wi-Fi is free."),
    ],
    "hotel_luggage_storage": [
        ("네, 맡아 드릴게요.", "Yes, we can hold it for you."),
        ("체크인 후에 맡겨 주세요.", "Please leave it after check-in."),
        ("보관증을 드릴게요.", "I will give you a storage ticket."),
    ],
    "hotel_extra_towel": [
        ("네, 가져다드릴게요.", "Yes, I will bring it to you."),
        ("몇 장 필요하세요?", "How many do you need?"),
        ("수건은 욕실에 있어요.", "The towels are in the bathroom."),
    ],
    "hotel_checkout_time": [
        ("오전 열한 시예요.", "It is 11 a.m."),
        ("한 시간 늦게 하셔도 돼요.", "You may check out one hour late."),
        ("짐은 프런트에 맡겨 주세요.", "Please leave your luggage at the front desk."),
    ],
    "hotel_room_problem": [
        ("어떤 문제예요?", "What is the problem?"),
        ("직원이 올라가 볼게요.", "A staff member will come up to check."),
        ("방을 바꿔 드릴게요.", "We will change your room."),
    ],
    "directions_restroom": [
        ("저쪽에 있어요.", "It is over there."),
        ("2층에 있어요.", "It is on the second floor."),
        ("직진하면 오른쪽이에요.", "Go straight; it is on the right."),
    ],
    "directions_convenience_store": [
        ("네, 바로 앞에 있어요.", "Yes, it is right in front."),
        ("이 건물 1층에 있어요.", "It is on the first floor of this building."),
        ("24시간 영업해요.", "It is open 24 hours."),
    ],
    "directions_walking_time": [
        ("십 분 정도 걸려요.", "It takes about ten minutes."),
        ("삼십 분쯤 걸려요.", "It takes about 30 minutes."),
        ("걸어가기에는 조금 멀어요.", "It is a little far to walk."),
    ],
    "directions_lost": [
        ("어디를 찾으세요?", "What are you looking for?"),
        ("지도를 보여 주세요.", "Please show me the map."),
        ("제가 안내해 드릴게요.", "I will show you the way."),
    ],
    "directions_nearby": [
        ("네, 걸어서 오 분이에요.", "Yes, it is a five-minute walk."),
        ("조금 멀어요.", "It is a little far."),
        ("지하철을 타는 게 좋아요.", "It is better to take the subway."),
    ],
    "shopping_price": [
        ("만 원이에요.", "It is 10,000 won."),
        ("할인 중이에요.", "It is on sale."),
        ("두 개에 만 오천 원이에요.", "Two are 15,000 won."),
    ],
    "shopping_try_on": [
        ("네, 입어 보세요.", "Yes, try it on."),
        ("탈의실은 저쪽이에요.", "The fitting room is over there."),
        ("새 상품으로 가져다드릴게요.", "I will bring you a new item."),
    ],
    "shopping_larger_size": [
        ("네, 이 사이즈가 더 커요.", "Yes, this size is larger."),
        ("죄송하지만 이게 가장 큰 사이즈예요.", "Sorry, this is the largest size."),
        ("한 사이즈 큰 것도 있어요.", "We also have one size larger."),
    ],
    "shopping_different_color": [
        ("검은색도 있어요.", "We also have black."),
        ("빨간색은 품절이에요.", "The red one is sold out."),
        ("이 색이 제일 인기 있어요.", "This color is the most popular."),
    ],
    "shopping_tax_refund": [
        ("네, 여권 보여 주세요.", "Yes, please show your passport."),
        ("구매 금액이 만 원 이상이어야 해요.", "The purchase amount must be at least 10,000 won."),
        ("공항에서 환급받으실 수 있어요.", "You can receive the refund at the airport."),
    ],
    "cafe_eat_here": [
        ("네, 여기서 드세요.", "Yes, please eat here."),
        ("자리 먼저 잡아 주세요.", "Please get a seat first."),
        ("주문은 카운터에서 해 주세요.", "Please order at the counter."),
    ],
    "cafe_takeout": [
        ("네, 가능합니다.", "Yes, that is possible."),
        ("포장해 드릴게요.", "We will pack it for you."),
        ("몇 분 정도 걸려요.", "It takes a few minutes."),
    ],
    "cafe_iced_americano": [
        ("사이즈는 어떻게 드릴까요?", "What size would you like?"),
        ("뜨거운 걸로 드릴까요?", "Would you like it hot?"),
        ("주문 나왔습니다.", "Your order is ready."),
    ],
    "cafe_water_free": [
        ("네, 무료예요.", "Yes, it is free."),
        ("생수는 유료예요.", "Bottled water costs extra."),
        ("정수기는 저쪽에 있어요.", "The water dispenser is over there."),
    ],
    "cafe_split_bill": [
        ("네, 따로 계산해 드릴게요.", "Yes, I will split the bill."),
        ("한 분씩 결제해 주세요.", "Please pay one person at a time."),
        ("카드는 따로 사용하실 수 있어요.", "You can use separate cards."),
    ],
    "emergency_pharmacy": [
        ("이 길로 쭉 가세요.", "Go straight along this road."),
        ("건너편에 있어요.", "It is across the street."),
        ("여기서 가까워요.", "It is close from here."),
    ],
    "emergency_hospital": [
        ("택시 타고 가세요.", "Take a taxi there."),
        ("응급실은 저쪽이에요.", "The emergency room is over there."),
        ("구급차를 불러 드릴까요?", "Shall I call an ambulance?"),
    ],
    "emergency_help": [
        ("무슨 일이세요?", "What happened?"),
        ("괜찮으세요?", "Are you okay?"),
        ("경찰을 불러 드릴까요?", "Shall I call the police?"),
    ],
    "emergency_unwell": [
        ("괜찮으세요?", "Are you okay?"),
        ("앉아서 쉬세요.", "Sit down and rest."),
        ("병원에 가 보세요.", "Please try going to a hospital."),
    ],
    "emergency_lost_passport": [
        ("경찰서에 가 보세요.", "Please try going to the police station."),
        ("여권을 언제 잃어버리셨어요?", "When did you lose your passport?"),
        ("대사관에 연락해 보세요.", "Try contacting your embassy."),
    ],
}


def init_state() -> None:
    st.session_state.setdefault("mastered", set())
    st.session_state.setdefault("favorites", set())
    st.session_state.setdefault("current_phrase_id", PHRASES[0]["id"])


def phrase_by_id(phrase_id: str) -> dict:
    return next(phrase for phrase in PHRASES if phrase["id"] == phrase_id)


def phrase_options(category: str, level: str, favorites_only: bool) -> list[dict]:
    phrases = PHRASES
    if category != "All":
        phrases = [phrase for phrase in phrases if phrase["category"] == category]
    if level != "All":
        phrases = [phrase for phrase in phrases if phrase["level"] == level]
    if favorites_only:
        phrases = [phrase for phrase in phrases if phrase["id"] in st.session_state.favorites]
    return phrases or PHRASES


def tts_button(text: str, button_label: str, key: str, rate: float = 0.78) -> None:
    safe_text = escape(text)
    safe_label = escape(button_label)
    safe_key = escape(key)
    components.html(
        f"""
        <button id="speak-{safe_key}" class="speak-button">{safe_label}</button>
        <script>
        const button = document.getElementById("speak-{safe_key}");
        const synthesis = "speechSynthesis" in window ? window.speechSynthesis : null;
        const voiceStorageKey = "korean-service-phrase-voice";
        const preferredVoiceNames = [
            "natural",
            "neural",
            "enhanced",
            "premium",
            "sunhi",
            "hyunsu",
            "yuna",
            "sora",
            "heami",
        ];
        let koreanVoices = [];

        const loadKoreanVoices = () => {{
            if (!synthesis) return;
            try {{
                koreanVoices = synthesis.getVoices().filter((voice) =>
                    voice.lang.toLowerCase().startsWith("ko")
                );
            }} catch (error) {{
                koreanVoices = [];
            }}
        }};
        if (synthesis) {{
            loadKoreanVoices();
            synthesis.addEventListener("voiceschanged", loadKoreanVoices);
        }}

        const chooseKoreanVoice = () => {{
            const voices = koreanVoices.length
                ? koreanVoices
                : (synthesis ? synthesis.getVoices() : []).filter((voice) =>
                    voice.lang.toLowerCase().startsWith("ko")
                );
            let savedVoiceName = "";
            try {{
                savedVoiceName = window.localStorage.getItem(voiceStorageKey) || "";
            }} catch (error) {{
                savedVoiceName = "";
            }}
            const savedVoice = voices.find((voice) => voice.name === savedVoiceName);
            if (savedVoice) return savedVoice;
            return [...voices].sort((left, right) => {{
                const leftName = left.name.toLowerCase();
                const rightName = right.name.toLowerCase();
                const leftScore = preferredVoiceNames.reduce(
                    (score, word, index) => score + (leftName.includes(word) ? 100 - index : 0),
                    0
                );
                const rightScore = preferredVoiceNames.reduce(
                    (score, word, index) => score + (rightName.includes(word) ? 100 - index : 0),
                    0
                );
                return rightScore - leftScore;
            }})[0];
        }};

        button.onclick = () => {{
            if (!synthesis || !("SpeechSynthesisUtterance" in window)) return;
            synthesis.cancel();
            const utterance = new SpeechSynthesisUtterance("{safe_text}");
            utterance.lang = "ko-KR";
            utterance.rate = {rate};
            utterance.pitch = 1;
            const koreanVoice = chooseKoreanVoice();
            if (koreanVoice) utterance.voice = koreanVoice;
            synthesis.speak(utterance);
        }};
        </script>
        <style>
        .speak-button {{
            width: 100%;
            border: 1px solid #275a53;
            background: #275a53;
            color: white;
            border-radius: 8px;
            padding: 0.72rem 0.9rem;
            font: 600 0.96rem -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            cursor: pointer;
        }}
        .speak-button:hover {{
            background: #1f4842;
            border-color: #1f4842;
        }}
        </style>
        """,
        height=56,
    )


def korean_voice_selector() -> None:
    components.html(
        """
        <div class="voice-picker">
            <label for="korean-voice-select">Pronunciation voice</label>
            <select id="korean-voice-select">
                <option value="">Loading Korean voices...</option>
            </select>
        </div>
        <script>
        const voiceSelect = document.getElementById("korean-voice-select");
        const synthesis = "speechSynthesis" in window ? window.speechSynthesis : null;
        const voiceStorageKey = "korean-service-phrase-voice";
        let attempts = 0;

        const getKoreanVoices = () => {
            if (!synthesis) return [];
            try {
                return synthesis.getVoices()
                    .filter((voice) => voice.lang.toLowerCase().startsWith("ko"))
                    .sort((left, right) => left.name.localeCompare(right.name));
            } catch (error) {
                return [];
            }
        };

        const readVoicePreference = () => {
            try {
                return window.localStorage.getItem(voiceStorageKey) || "";
            } catch (error) {
                return "";
            }
        };

        const saveVoicePreference = (voiceName) => {
            try {
                if (voiceName) window.localStorage.setItem(voiceStorageKey, voiceName);
                else window.localStorage.removeItem(voiceStorageKey);
            } catch (error) {
                // Some embedded browser contexts do not expose local storage.
            }
        };

        const renderKoreanVoices = (finalAttempt = false) => {
            const voices = getKoreanVoices();
            if (!voices.length && !finalAttempt) return false;
            const savedVoice = readVoicePreference();

            voiceSelect.innerHTML = "";
            const automaticOption = document.createElement("option");
            automaticOption.value = "";
            automaticOption.textContent = synthesis
                ? "Automatic best voice"
                : "Browser speech unavailable";
            voiceSelect.appendChild(automaticOption);

            voices.forEach((voice) => {
                const option = document.createElement("option");
                option.value = voice.name;
                option.textContent = `${voice.name} (${voice.lang})`;
                voiceSelect.appendChild(option);
            });

            voiceSelect.value = voices.some((voice) => voice.name === savedVoice)
                ? savedVoice
                : "";
            if (!voices.length && synthesis) {
                automaticOption.textContent = "No Korean voices found";
            }
            return true;
        };

        const retryVoiceLoad = () => {
            if (renderKoreanVoices()) return;
            attempts += 1;
            if (attempts < 40) setTimeout(retryVoiceLoad, 250);
            else renderKoreanVoices(true);
        };

        voiceSelect.addEventListener("change", () => saveVoicePreference(voiceSelect.value));
        if (synthesis) {
            synthesis.addEventListener("voiceschanged", () => renderKoreanVoices(true));
            retryVoiceLoad();
        } else {
            renderKoreanVoices(true);
        }
        </script>
        <style>
        .voice-picker {
            display: grid;
            gap: 0.35rem;
            font: 0.86rem -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }
        .voice-picker label {
            color: #2e3834;
            font-weight: 600;
        }
        .voice-picker select {
            width: 100%;
            min-height: 2.45rem;
            border: 1px solid #b9afa1;
            border-radius: 7px;
            background: #fffaf1;
            color: #1f2523;
            padding: 0.35rem 0.5rem;
            font: inherit;
        }
        </style>
        """,
        height=86,
    )


def render_word_table(words: list[tuple[str, str, str, str]]) -> None:
    rows = [
        {
            "Hangul": word,
            "English pronunciation": pronunciation,
            "Meaning": meaning,
            "How it works": note,
        }
        for word, pronunciation, meaning, note in words
    ]
    st.dataframe(rows, hide_index=True, width="stretch")


def render_conversations(phrase: dict) -> None:
    responses = CONVERSATION_RESPONSES[phrase["id"]]
    with st.expander("Example conversations"):
        st.write("Hear how the same phrase might fit into a real service interaction.")
        for index, (response, translation) in enumerate(responses, start=1):
            st.markdown(f"**Example {index}**")
            st.markdown(f"**You (Hangul):** {phrase['korean']}")
            st.caption(f"English pronunciation: {phrase['romanization']}")
            st.caption(f"English translation: {phrase['english']}")
            st.markdown(f"**Staff (Hangul):** {response}")
            st.caption(f"English pronunciation: {romanize_korean(response)}")
            st.caption(f"English translation: {translation}")
            if index != len(responses):
                st.divider()


def render_phrase_card(phrase: dict) -> None:
    mastered = phrase["id"] in st.session_state.mastered
    favorite = phrase["id"] in st.session_state.favorites

    top_left, top_right = st.columns([0.72, 0.28], vertical_alignment="top")
    with top_left:
        st.caption(f'{phrase["category"]} · {phrase["level"]}')
        st.caption("English translation")
        st.markdown(f"## {phrase['english']}")
        st.caption("Hangul")
        st.markdown(f"<div class='korean-line'>{phrase['korean']}</div>", unsafe_allow_html=True)
        st.caption("English pronunciation")
        st.markdown(f"<div class='romanization'>{phrase['romanization']}</div>", unsafe_allow_html=True)
    with top_right:
        if st.button("Favorite" if not favorite else "Favorited", width="stretch"):
            if favorite:
                st.session_state.favorites.remove(phrase["id"])
            else:
                st.session_state.favorites.add(phrase["id"])
            st.rerun()
        if st.button("Mark learned" if not mastered else "Learned", width="stretch"):
            if mastered:
                st.session_state.mastered.remove(phrase["id"])
            else:
                st.session_state.mastered.add(phrase["id"])
            st.rerun()

    st.markdown(f"**When to use it:** {phrase['context']}")
    response_korean, response_translation = phrase["response"].split(" = ", 1)
    st.markdown(f"**Likely response (Hangul):** {response_korean}")
    st.caption(f"English pronunciation: {romanize_korean(response_korean)}")
    st.caption(f"English translation: {response_translation}")
    render_conversations(phrase)

    play_col, slow_col = st.columns(2)
    with play_col:
        tts_button(phrase["korean"], "Play natural pronunciation", f"{phrase['id']}-natural", rate=0.82)
    with slow_col:
        tts_button(phrase["slow"].replace(" / ", ". "), "Play slower practice version", f"{phrase['id']}-slow", rate=0.55)

    st.divider()
    tabs = st.tabs(["Pronunciation", "Word by word", "Record and compare"])

    with tabs[0]:
        st.markdown("### Speaking notes")
        for note in phrase["pronunciation"]:
            st.markdown(f"- {note}")

        st.markdown("### Practice rhythm")
        chunks = phrase["slow"].split(" / ")
        st.markdown(
            "<div class='chunks'>"
            + "".join(f"<span>{escape(chunk)}</span>" for chunk in chunks)
            + "</div>",
            unsafe_allow_html=True,
        )

    with tabs[1]:
        st.markdown("### Individual word explanation")
        render_word_table(phrase["words"])

    with tabs[2]:
        st.markdown("### Record your version")
        st.write("Record the sentence, then play it back and compare it with the Korean audio above.")
        if hasattr(st, "audio_input"):
            recording = st.audio_input("Record yourself saying the phrase")
            if recording is not None:
                st.audio(recording)
                st.success("Playback ready. Listen once to the model, then once to your recording.")
        else:
            st.warning(
                "This Streamlit version does not include voice recording. Install Streamlit 1.40 or newer."
            )


def render_drill(phrases: list[dict]) -> None:
    st.markdown("### Quick service drill")
    st.write("Cover the Korean line with your hand, say the phrase aloud, then reveal and play it.")

    index = st.slider("Phrase", 1, len(phrases), 1) - 1
    phrase = phrases[index]
    st.caption(f'{phrase["category"]} · {phrase["level"]}')
    st.markdown(f"**Prompt:** {phrase['english']}")

    with st.expander("Reveal Korean"):
        st.markdown(f"**Hangul:**")
        st.markdown(f"<div class='drill-korean'>{phrase['korean']}</div>", unsafe_allow_html=True)
        st.markdown(f"**English pronunciation:** {phrase['romanization']}")
        st.markdown(f"**English translation:** {phrase['english']}")
        tts_button(phrase["korean"], "Play phrase", f"drill-{phrase['id']}", rate=0.78)


def render_sidebar() -> tuple[str, str, bool, list[dict]]:
    categories = ["All"] + sorted({phrase["category"] for phrase in PHRASES})
    levels = ["All", "Starter", "Travel Ready"]

    st.sidebar.title("Korean Phrase Coach")
    st.sidebar.caption("For restaurants, spas, and service conversations in Korea.")

    with st.sidebar:
        st.markdown("#### Pronunciation")
        korean_voice_selector()

    category = st.sidebar.selectbox("Situation", categories)
    level = st.sidebar.selectbox("Level", levels)
    favorites_only = st.sidebar.checkbox("Show favorites only")
    filtered = phrase_options(category, level, favorites_only)

    learned_count = len(st.session_state.mastered)
    st.sidebar.progress(learned_count / len(PHRASES))
    st.sidebar.write(f"{learned_count} of {len(PHRASES)} phrases marked learned")

    return category, level, favorites_only, filtered


def render_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
        }
        .stApp {
            background: #f7f4ef;
            color: #1f2523;
        }
        [data-testid="stSidebar"] {
            background: #ece5d8;
            color: #1f2523;
        }
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"] {
            background: #f7f4ef;
            color: #1f2523;
        }
        [data-testid="stHeader"] {
            background: transparent;
        }
        [data-testid="stSidebar"] > div:first-child {
            background: #ece5d8;
        }
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] div {
            color: #1f2523;
        }
        label,
        p,
        [data-testid="stCaptionContainer"] {
            color: #2e3834;
        }
        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
            color: #17211e;
        }
        input,
        textarea,
        [data-baseweb="input"] > div,
        [data-baseweb="textarea"] > div {
            background: #fffaf1 !important;
            color: #1f2523 !important;
            border-color: #b9afa1 !important;
            -webkit-text-fill-color: #1f2523 !important;
        }
        input::placeholder,
        textarea::placeholder {
            color: #68716d !important;
            -webkit-text-fill-color: #68716d !important;
        }
        [data-baseweb="select"] > div {
            background: #fffaf1 !important;
            color: #1f2523 !important;
            border-color: #b9afa1 !important;
        }
        [data-baseweb="select"] div,
        [data-baseweb="select"] input,
        [data-baseweb="select"] span {
            color: #1f2523 !important;
            -webkit-text-fill-color: #1f2523 !important;
        }
        [data-baseweb="select"] svg {
            fill: #1f2523 !important;
        }
        [data-baseweb="popover"],
        [data-baseweb="menu"],
        [role="listbox"] {
            background: #fffaf1 !important;
            color: #1f2523 !important;
            border: 1px solid #b9afa1 !important;
        }
        [role="option"] {
            background: #fffaf1 !important;
            color: #1f2523 !important;
        }
        [role="option"]:hover,
        [role="option"][aria-selected="true"] {
            background: #e5eee9 !important;
            color: #173e38 !important;
        }
        [data-testid="stCheckbox"] label,
        [data-testid="stSlider"] label {
            color: #1f2523 !important;
        }
        [data-baseweb="tab-list"] {
            border-bottom-color: #c9c0b4 !important;
        }
        [data-baseweb="tab"] {
            color: #394641 !important;
        }
        [data-baseweb="tab"][aria-selected="true"] {
            color: #173e38 !important;
            border-bottom-color: #275a53 !important;
        }
        [data-testid="stExpander"] {
            background: #fffaf1;
            border-color: #c9c0b4;
        }
        [data-testid="stExpander"] summary,
        [data-testid="stExpander"] summary span {
            color: #1f2523 !important;
        }
        .korean-line {
            font-size: 2.45rem;
            line-height: 1.18;
            font-weight: 760;
            color: #111817;
            margin: 0.4rem 0 0.35rem;
            word-break: keep-all;
        }
        .romanization {
            font-size: 1.08rem;
            color: #59615e;
            margin-bottom: 1rem;
        }
        .chunks {
            display: flex;
            gap: 0.55rem;
            flex-wrap: wrap;
            margin-top: 0.5rem;
        }
        .chunks span {
            border: 1px solid #d2c5b3;
            background: #fffaf1;
            border-radius: 8px;
            padding: 0.5rem 0.7rem;
            font-size: 1.1rem;
            font-weight: 650;
        }
        .drill-korean {
            font-size: 2rem;
            font-weight: 760;
            line-height: 1.25;
            margin-bottom: 0.25rem;
        }
        div[data-testid="stMetric"] {
            background: #fffaf1;
            border: 1px solid #d8cebf;
            border-radius: 8px;
            padding: 0.75rem;
        }
        div[data-testid="stMetric"] label,
        div[data-testid="stMetric"] [data-testid="stMetricValue"],
        div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
            color: #1f2523 !important;
        }
        .stButton > button {
            background: #275a53 !important;
            color: #ffffff !important;
            border: 1px solid #275a53 !important;
            border-radius: 8px;
            min-height: 2.65rem;
        }
        .stButton > button:hover {
            background: #1f4842 !important;
            border-color: #1f4842 !important;
            color: #ffffff !important;
        }
        .stButton > button p,
        .stButton > button span {
            color: #ffffff !important;
        }
        div[data-testid="stAlert"] {
            color: #1f2523 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    init_state()
    render_styles()
    _, _, _, filtered = render_sidebar()

    st.title("Korean phrases for restaurants and spas")
    st.write(
        "Practice polite Korean phrases, hear Korean pronunciation, record your voice, and learn what each word is doing."
    )

    phrase_labels = [
        f"{phrase['english']}  ·  {phrase['korean']}"
        for phrase in filtered
    ]
    phrase_ids = [phrase["id"] for phrase in filtered]

    if st.session_state.current_phrase_id not in phrase_ids:
        st.session_state.current_phrase_id = phrase_ids[0]

    selected_label = st.selectbox(
        "Choose a phrase",
        phrase_labels,
        index=phrase_ids.index(st.session_state.current_phrase_id),
    )
    selected_index = phrase_labels.index(selected_label)
    st.session_state.current_phrase_id = phrase_ids[selected_index]
    selected_phrase = phrase_by_id(st.session_state.current_phrase_id)

    phrase_tab, drill_tab, list_tab = st.tabs(["Phrase coach", "Drill", "Phrase list"])
    with phrase_tab:
        render_phrase_card(selected_phrase)

    with drill_tab:
        render_drill(filtered)

    with list_tab:
        rows = [
            {
                "Situation": phrase["category"],
                "Level": phrase["level"],
                "English translation": phrase["english"],
                "Hangul": phrase["korean"],
                "English pronunciation": phrase["romanization"],
                "Learned": "Yes" if phrase["id"] in st.session_state.mastered else "",
            }
            for phrase in PHRASES
        ]
        st.dataframe(rows, hide_index=True, width="stretch")


if __name__ == "__main__":
    main()
