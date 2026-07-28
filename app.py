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
]


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
            koreanVoices = window.speechSynthesis.getVoices().filter((voice) =>
                voice.lang.toLowerCase().startsWith("ko")
            );
        }};
        loadKoreanVoices();
        window.speechSynthesis.addEventListener("voiceschanged", loadKoreanVoices);

        const chooseKoreanVoice = () => {{
            const voices = koreanVoices.length
                ? koreanVoices
                : window.speechSynthesis.getVoices().filter((voice) =>
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
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance("{safe_text}");
            utterance.lang = "ko-KR";
            utterance.rate = {rate};
            utterance.pitch = 1;
            const koreanVoice = chooseKoreanVoice();
            if (koreanVoice) utterance.voice = koreanVoice;
            window.speechSynthesis.speak(utterance);
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
        const voiceStorageKey = "korean-service-phrase-voice";

        const readVoicePreference = () => {{
            try {{
                return window.localStorage.getItem(voiceStorageKey) || "";
            }} catch (error) {{
                return "";
            }}
        }};

        const saveVoicePreference = (voiceName) => {{
            try {{
                if (voiceName) window.localStorage.setItem(voiceStorageKey, voiceName);
                else window.localStorage.removeItem(voiceStorageKey);
            }} catch (error) {{
                // Some embedded browser contexts do not expose local storage.
            }}
        }};

        const renderKoreanVoices = () => {{
            const voices = window.speechSynthesis.getVoices()
                .filter((voice) => voice.lang.toLowerCase().startsWith("ko"))
                .sort((left, right) => left.name.localeCompare(right.name));
            const savedVoice = readVoicePreference();

            voiceSelect.innerHTML = "";
            const automaticOption = document.createElement("option");
            automaticOption.value = "";
            automaticOption.textContent = "Automatic best voice";
            voiceSelect.appendChild(automaticOption);

            voices.forEach((voice) => {{
                const option = document.createElement("option");
                option.value = voice.name;
                option.textContent = `${{voice.name}} (${{voice.lang}})`;
                voiceSelect.appendChild(option);
            }});

            voiceSelect.value = voices.some((voice) => voice.name === savedVoice)
                ? savedVoice
                : "";
            if (!voices.length) {{
                automaticOption.textContent = "No Korean voices found";
            }}
        }};

        voiceSelect.addEventListener("change", () => saveVoicePreference(voiceSelect.value));
        renderKoreanVoices();
        window.speechSynthesis.addEventListener("voiceschanged", renderKoreanVoices);
        </script>
        <style>
        .voice-picker {{
            display: grid;
            gap: 0.35rem;
            font: 0.86rem -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }}
        .voice-picker label {{
            color: #2e3834;
            font-weight: 600;
        }}
        .voice-picker select {{
            width: 100%;
            min-height: 2.45rem;
            border: 1px solid #b9afa1;
            border-radius: 7px;
            background: #fffaf1;
            color: #1f2523;
            padding: 0.35rem 0.5rem;
            font: inherit;
        }}
        </style>
        """,
        height=86,
    )


def render_word_table(words: list[tuple[str, str, str, str]]) -> None:
    rows = [
        {
            "Korean": word,
            "Pronunciation": pronunciation,
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
            st.markdown(f"**You:** {phrase['korean']}  \n{phrase['english']}")
            st.markdown(f"**Staff:** {response}  \n{translation}")
            if index != len(responses):
                st.divider()


def render_phrase_card(phrase: dict) -> None:
    mastered = phrase["id"] in st.session_state.mastered
    favorite = phrase["id"] in st.session_state.favorites

    top_left, top_right = st.columns([0.72, 0.28], vertical_alignment="top")
    with top_left:
        st.caption(f'{phrase["category"]} · {phrase["level"]}')
        st.markdown(f"## {phrase['english']}")
        st.markdown(f"<div class='korean-line'>{phrase['korean']}</div>", unsafe_allow_html=True)
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
    st.markdown(f"**Likely response:** {phrase['response']}")
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
        st.markdown(f"<div class='drill-korean'>{phrase['korean']}</div>", unsafe_allow_html=True)
        st.markdown(phrase["romanization"])
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
                "English": phrase["english"],
                "Korean": phrase["korean"],
                "Pronunciation": phrase["romanization"],
                "Learned": "Yes" if phrase["id"] in st.session_state.mastered else "",
            }
            for phrase in PHRASES
        ]
        st.dataframe(rows, hide_index=True, width="stretch")


if __name__ == "__main__":
    main()
