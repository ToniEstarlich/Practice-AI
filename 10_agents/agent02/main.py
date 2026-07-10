import requests

# -----------------------------
# 🧠 OLLAMA (BRAIN)
# -----------------------------

def call_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["response"]


# -----------------------------
# ⚙️ TOOL: SAVE FILE
# -----------------------------

def save_html(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


# -----------------------------
# 🤖 AGENT
# -----------------------------

class LandingPageAgent:

    def generate_landing_page(self, idea):

       prompt = f"""
You are an award-winning Senior Front-End Developer, UI/UX Designer, and Technical SEO specialist.

Your task is to generate a COMPLETE production-quality landing page.

The page must be beautiful enough to impress a real client.

--------------------------------------------------
PROJECT
--------------------------------------------------

Business:
{idea}

--------------------------------------------------
TECH STACK
--------------------------------------------------

Generate ONE complete HTML file containing:

- HTML5
- CSS inside <style>
- jQuery (CDN)
- Google Fonts
- Font Awesome CDN
- Vanilla JavaScript only if necessary
- No frameworks
- No external CSS files

Return ONLY the HTML.

--------------------------------------------------
DESIGN STYLE
--------------------------------------------------

Create a premium modern SaaS-style landing page.

Style requirements:

• Beautiful spacing
• Soft shadows
• Rounded corners
• Glassmorphism where appropriate
• Gradient accents
• Large typography
• Clean layout
• High-end startup appearance
• Professional animations
• Elegant hover effects
• Modern buttons
• Cards with depth
• Smooth scrolling
• Sticky navbar
• Mobile-first design
• Excellent white space
• Beautiful icons
• High quality placeholder images from:
https://images.pexels.com/

Use a modern color palette.

Example palette:

Primary:
#2563EB

Secondary:
#7C3AED

Accent:
#06B6D4

Background:
#F8FAFC

Dark:
#0F172A

Text:
#334155

--------------------------------------------------
TYPOGRAPHY
--------------------------------------------------

Use Google Fonts.

Examples:

Poppins
Inter
Manrope

Use clear typography hierarchy.

--------------------------------------------------
LAYOUT
--------------------------------------------------

Include:

✔ Sticky navigation bar

- Logo
- Home
- Services
- About
- Testimonials
- Contact
- CTA button

✔ Hero section

- Large headline
- Supporting text
- Two CTA buttons
- Hero illustration/image

✔ Trusted By section

✔ Features

Display as modern cards.

✔ Benefits section

✔ Statistics section

✔ How It Works

✔ Pricing cards (3)

✔ Testimonials

✔ FAQ Accordion

✔ Contact form

Name
Email
Message

✔ CTA Banner

✔ Footer

Include:

- Links
- Social icons
- Copyright
- Privacy
- Terms

--------------------------------------------------
RESPONSIVE DESIGN
--------------------------------------------------

Must work perfectly on:

Desktop

Tablet

Mobile

Use:

Flexbox
CSS Grid
Media Queries

Navbar becomes hamburger menu.

Cards stack correctly.

Images resize properly.

No horizontal scrolling.

--------------------------------------------------
ANIMATIONS
--------------------------------------------------

Use jQuery animations.

Include:

fadeIn()

slideDown()

smooth scrolling

animated navbar

scroll reveal

hover transitions

button ripple effect (CSS)

floating hero image

--------------------------------------------------
SEO
--------------------------------------------------

Include:

<title>

<meta name="description">

<meta name="keywords">

<meta name="author">

<meta property="og:title">

<meta property="og:description">

<meta property="og:image">

<meta property="og:type">

Twitter Card tags

Canonical URL

Proper heading hierarchy

One H1

Semantic HTML

<header>

<nav>

<main>

<section>

<footer>

Alt text on every image

Lazy loading

Fast loading CSS

--------------------------------------------------
ACCESSIBILITY
--------------------------------------------------

Use:

ARIA labels

High contrast

Keyboard navigation

Accessible buttons

Accessible forms

Proper labels

--------------------------------------------------
CODE QUALITY
--------------------------------------------------

Write clean, readable code.

Comment every major section.

Indent correctly.

Avoid duplicated CSS.

Use CSS variables.

Create reusable button classes.

Use reusable card classes.

--------------------------------------------------
VISUAL QUALITY
--------------------------------------------------

The final page should look similar in quality to:

Stripe

Vercel

Linear

Framer

Webflow templates

Apple

Modern SaaS startups

--------------------------------------------------
IMPORTANT
--------------------------------------------------

Return ONLY the complete HTML document.

Do NOT explain anything.

Do NOT use markdown.

Do NOT wrap the code in ```.

The first line must be:

<!DOCTYPE html>
""" 
       return call_ollama(prompt)


    def run(self, idea):

        print("\n🚀 LANDING PAGE AGENT STARTED\n")

        print("🧠 Generating HTML...\n")
        html = self.generate_landing_page(idea)

        print("💾 Saving file...\n")
        save_html("landing.html", html)

        print("\n✅ DONE -> landing.html created")


# -----------------------------
# ▶️ RUN
# -----------------------------

if __name__ == "__main__":

    agent = LandingPageAgent()

    idea = input("Enter landing page idea:\n> ")

    agent.run(idea)