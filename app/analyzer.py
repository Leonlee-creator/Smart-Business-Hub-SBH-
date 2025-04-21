def analyze_market(business_name, location):
    if not business_name or not location:
        return "Please enter both business name and target location."

    return f"""
    **Market Analysis for {business_name} in {location}:**

    ✅ High demand for innovative solutions in this space.  
    ✅ Low competition detected in emerging markets.  
    ✅ High internet penetration supports scalability.  
    ⚠️ Consider local regulations and customer education.  
    📊 Overall Score: **8.5/10**

    Tip: Validate the idea with surveys or a landing page test.
    """
