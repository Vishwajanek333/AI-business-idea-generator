import json

class AIService:
    def __init__(self):
        print("[AI_SERVICE] Using MOCK mode (no OpenAI calls)")
    
    def generate_business_ideas(self, keywords: str, industry: str, num_ideas: int) -> list:
        """Generate mock business ideas for testing"""
        print(f"\n[AI_SERVICE] Generating {num_ideas} MOCK ideas")
        print(f"[AI_SERVICE] Keywords: {keywords}")
        print(f"[AI_SERVICE] Industry: {industry}")
        
        mock_ideas = [
            {
                "title": f"AI-Powered {industry} Platform",
                "description": f"An innovative {industry} solution using {keywords}. This platform leverages artificial intelligence to provide personalized solutions for professionals.",
                "business_model": "SaaS subscription model with tiered pricing starting at 99 USD per month for individuals",
                "target_audience": "Tech-savvy professionals, students, and organizations looking for advanced learning solutions",
                "swot_analysis": "Strengths: Advanced AI, user-friendly interface. Weaknesses: High development cost. Opportunities: Growing market demand. Threats: Competition from established players",
                "market_potential": "The global AI market is projected to reach 1.8 trillion USD by 2030, with strong growth in education and enterprise sectors",
                "keywords": keywords
            },
            {
                "title": f"Intelligent {industry} Assistant",
                "description": f"A smart virtual assistant powered by {keywords} technology designed specifically for {industry} professionals. It automates routine tasks and provides intelligent recommendations.",
                "business_model": "Freemium model with free basic tier and premium features at 19.99 USD per month",
                "target_audience": "Busy professionals in {industry}, academic institutions, and corporate training departments",
                "swot_analysis": "Strengths: Automation, 24/7 availability. Weaknesses: Initial setup complexity. Opportunities: B2B partnerships. Threats: Alternative solutions",
                "market_potential": "Expected market size of 500 billion USD or more by 2025 with 40 percent annual growth rate",
                "keywords": keywords
            },
            {
                "title": f"Blockchain-Based {industry} Network",
                "description": f"A decentralized {industry} network using {keywords} to ensure transparency and security. Connects learners, experts, and organizations in a trusted ecosystem.",
                "business_model": "Token-based economy with transaction fees and premium membership options",
                "target_audience": "Forward-thinking organizations, tech enthusiasts, and institutions seeking decentralized solutions",
                "swot_analysis": "Strengths: Decentralized, transparent. Weaknesses: Regulatory uncertainty. Opportunities: First-mover advantage. Threats: Blockchain adoption barriers",
                "market_potential": "Blockchain in {industry} sector estimated at 200 billion USD or more opportunity with emerging regulatory frameworks",
                "keywords": keywords
            }
        ]
        
        print(f"[AI_SERVICE] Generated {len(mock_ideas[:num_ideas])} ideas successfully\n")
        return mock_ideas[:num_ideas]