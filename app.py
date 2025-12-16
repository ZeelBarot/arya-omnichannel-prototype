import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie
from products import products

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="ARYA – Omnichannel AI Stylist",
    layout="centered"
)

# =====================================================
# SESSION STATE
# =====================================================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "channel" not in st.session_state:
    st.session_state.channel = "Mobile"

if "img_index" not in st.session_state:
    st.session_state.img_index = 0

# =====================================================
# GLOBAL STYLES
# =====================================================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #0F172A, #020617);
    color: white;
}

.hero {
    background: linear-gradient(90deg, #6D28D9, #F97316);
    padding: 28px;
    border-radius: 26px;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
}

.badge {
    background: #22C55E;
    color: black;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
    display: inline-block;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    margin-top: -24px;
}

.fade {
    animation: fadeIn 0.9s ease-in;
}

button {
    background-color: #6D28D9 !important;
    color: white !important;
    border-radius: 14px !important;
    font-weight: 600 !important;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================
st.markdown("""
<div class="hero fade">
ARYA – Omnichannel AI Stylist 👗<br>
<span style="font-size:16px;font-weight:500;">
Powered by Agentic AI for Modern Retail
</span>
</div>
""", unsafe_allow_html=True)

st.caption("✨ AI-curated fashion with emotion & sustainability")

# =====================================================
# CHANNEL INDICATOR
# =====================================================
st.markdown(
    f"<span class='badge'>🟢 Channel: {st.session_state.channel}</span>",
    unsafe_allow_html=True
)

# =====================================================
# LOAD LOTTIE
# =====================================================
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

arya_lottie = load_lottie(
    "https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json"
)

st_lottie(arya_lottie, height=260, speed=1, loop=True)

# =====================================================
# CHAT TYPING BUBBLES
# =====================================================
chat_lines = [
    "Hi! I’m Arya 👋",
    "I’ll help you style the perfect festive look ✨",
    "I also prioritize eco-friendly fashion 🌿"
]

for line in chat_lines:
    with st.chat_message("assistant"):
        with st.spinner("Arya is typing..."):
            time.sleep(0.7)
        st.write(line)

# =====================================================
# FAKE AI THINKING
# =====================================================
with st.spinner("Arya is curating outfits just for you ✨"):
    time.sleep(1)

# =====================================================
# HERO PRODUCTS (2 ONLY)
# =====================================================
st.markdown("## ✨ Curated Just for You")

hero_products = products[:2]

for p in hero_products:

    st.markdown("## ✨ Curated Just for You")

hero_products = products[:2]

for p in hero_products:

    # ---------- IMAGE CAROUSEL (SAFE) ----------
    img_index = st.radio(
        "",
        range(len(p["images"])),
        horizontal=True,
        key=f"img_{p['id']}"
    )

    st.image(p["images"][img_index], use_container_width=True)

    # ---------- PRODUCT INFO (NO HTML LEAK) ----------
    st.markdown(
        f"<span class='badge'>{p['tag']}</span>",
        unsafe_allow_html=True
    )

    st.subheader(p["name"])
    st.write(f"₹{p['price']}")
    st.caption("Hand-picked by Arya for your style ✨")

    # ---------- ACTION ----------
    if p["stock"] == 0:
        st.warning("Arya says: This piece is currently unavailable 😕")
    else:
        if st.button("💜 Add to My Style Bag", key=p["id"]):
            if p not in st.session_state.cart:
                st.session_state.cart.append(p)
                st.success("Added by Arya ✨")

    st.markdown("---")


# =====================================================
# SUSTAINABILITY IMPACT
# =====================================================
if st.session_state.cart:
    eco_items = [i for i in st.session_state.cart if i["tag"] == "Sustainable"]
    impact = min(len(eco_items) * 30, 100)

    st.markdown("### 🌿 Sustainability Impact")
    st.progress(impact)
    st.caption(
        f"By choosing sustainable fashion, you reduced approx. {impact}% carbon impact 🌍"
    )

# =====================================================
# CART EXPERIENCE
# =====================================================
st.markdown("## 👜 Your Style Bag")

if st.session_state.cart:
    total = sum(i["price"] for i in st.session_state.cart)

    st.markdown(f"""
    <div class="fade" style="
        background:linear-gradient(135deg,#6D28D9,#F97316);
        border-radius:24px;
        padding:24px;
        color:white;
    ">
        <h3>Total Look Value</h3>
        <h1>₹{total}</h1>
        <p>Arya curated this look just for you 💫</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("Arya is waiting to build your perfect look ✨")

# =====================================================
# OMNICHANNEL WOW
# =====================================================
st.markdown("---")

if st.button("📲 Continue This Look In-Store"):
    st.session_state.channel = "Kiosk"
    st.success("Arya synced your look to the in-store kiosk 🏬")

# =====================================================
# AUTO IMAGE ROTATION (ANIMATION)
# =====================================================
time.sleep(1.4)
st.session_state.img_index += 1
st.rerun()
