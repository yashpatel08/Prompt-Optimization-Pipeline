"""
NOTE: Pricing changes frequently. Re-verify before relying on this for
billing-critical code. Legacy/deprecated models are marked accordingly.
"""

from app.pricing.pricing import ModelPricing

PRICING = {

    # ============================================================
    # LOCAL MODELS (self-hosted, no API cost)
    # ============================================================
    "qwen3:4b": ModelPricing(
        input_cost_per_million=0,
        output_cost_per_million=0,
    ),

    "gemma3:4b": ModelPricing(
        input_cost_per_million=0,
        output_cost_per_million=0,
    ),

    # ============================================================
    # ANTHROPIC — Claude (current generation, July 2026)
    # ============================================================
    "claude-opus-4-8": ModelPricing(
        input_cost_per_million=5.00,
        output_cost_per_million=25.00,
    ),

    "claude-sonnet-5": ModelPricing(
        # Intro pricing $2/$10 through Aug 31, 2026; standard rate $3/$15 after
        input_cost_per_million=2.00,
        output_cost_per_million=10.00,
    ),

    "claude-haiku-4-5": ModelPricing(
        input_cost_per_million=1.00,
        output_cost_per_million=5.00,
    ),

    # Mythos-tier (limited access / Project Glasswing + safety-hardened variant)
    "claude-fable-5": ModelPricing(
        input_cost_per_million=10.00,
        output_cost_per_million=50.00,
    ),

    # ============================================================
    # OPENAI — GPT-5.x flagship family (July 2026)
    # ============================================================
    "gpt-5.6-sol": ModelPricing(
        input_cost_per_million=5.00,
        output_cost_per_million=30.00,
    ),

    "gpt-5.6-terra": ModelPricing(
        input_cost_per_million=2.50,
        output_cost_per_million=15.00,
    ),

    "gpt-5.6-luna": ModelPricing(
        input_cost_per_million=1.00,
        output_cost_per_million=6.00,
    ),

    "gpt-5.5": ModelPricing(
        input_cost_per_million=5.00,
        output_cost_per_million=30.00,
    ),

    "gpt-5.5-pro": ModelPricing(
        input_cost_per_million=30.00,
        output_cost_per_million=180.00,
    ),

    "gpt-5.4": ModelPricing(
        input_cost_per_million=2.50,
        output_cost_per_million=15.00,
    ),

    "gpt-5.4-mini": ModelPricing(
        input_cost_per_million=0.75,
        output_cost_per_million=4.50,
    ),

    "gpt-5.4-nano": ModelPricing(
        input_cost_per_million=0.20,
        output_cost_per_million=1.25,
    ),

    "gpt-5.4-pro": ModelPricing(
        input_cost_per_million=30.00,
        output_cost_per_million=180.00,
    ),

    # ---- Legacy / still-supported OpenAI models ----
    "gpt-4.1": ModelPricing(
        input_cost_per_million=2.00,
        output_cost_per_million=8.00,
    ),

    "gpt-4.1-mini": ModelPricing(
        input_cost_per_million=0.40,
        output_cost_per_million=1.60,
    ),

    "gpt-4.1-nano": ModelPricing(
        input_cost_per_million=0.10,
        output_cost_per_million=0.40,
    ),

    "gpt-4o": ModelPricing(
        input_cost_per_million=2.50,
        output_cost_per_million=10.00,
    ),

    "gpt-4o-mini": ModelPricing(
        input_cost_per_million=0.15,
        output_cost_per_million=0.60,
    ),

    "o3": ModelPricing(
        input_cost_per_million=2.00,
        output_cost_per_million=8.00,
    ),

    "o4-mini": ModelPricing(
        input_cost_per_million=1.10,
        output_cost_per_million=4.40,
    ),

    # ============================================================
    # GOOGLE — Gemini (July 2026)
    # ============================================================
    "gemini-3.1-pro": ModelPricing(
        # <=200K context; jumps to $4/$18 above 200K
        input_cost_per_million=2.00,
        output_cost_per_million=12.00,
    ),

    "gemini-3.5-flash": ModelPricing(
        input_cost_per_million=1.50,
        output_cost_per_million=9.00,
    ),

    "gemini-3-flash": ModelPricing(
        input_cost_per_million=0.50,
        output_cost_per_million=3.00,
    ),

    "gemini-3.1-flash-lite": ModelPricing(
        input_cost_per_million=0.25,
        output_cost_per_million=1.50,
    ),

    # ---- Legacy Gemini (retiring Oct 16, 2026) ----
    "gemini-2.5-flash-lite": ModelPricing(
        input_cost_per_million=0.10,
        output_cost_per_million=0.40,
    ),
}