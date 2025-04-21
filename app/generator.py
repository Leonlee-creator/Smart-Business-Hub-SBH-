import random

def generate_business_idea(category, custom_keywords):
    tech_ideas = [
        "AI-powered tutoring platform for students",
        "Mobile app that tracks personal carbon footprint",
        "Freelancer marketplace for African creatives"
    ]
    health_ideas = [
        "Affordable telehealth app for remote villages",
        "Fitness tracking wearable for older adults",
        "Online mental wellness platform for teens"
    ]
    finance_ideas = [
        "Crypto savings app for beginners",
        "Smart budgeting tool for low-income households",
        "P2P lending app for African small businesses"
    ]
    categories = {
        "Tech": tech_ideas,
        "Health": health_ideas,
        "Finance": finance_ideas,
        "E-commerce": ["Online thrift store", "Eco-friendly packaging store", "B2B bulk supply app"],
        "Education": ["Skill-based learning platform", "Language learning through music", "AI mentor app"]
    }

    if category == "Custom" and custom_keywords:
        return f"A custom business focused on {custom_keywords.strip().title()}"
    
    idea_list = categories.get(category, ["Digital startup idea"])
    return random.choice(idea_list)
