# stripe_config.py
import stripe
import os

# Load the Stripe API key from an environment variable
stripe.api_key = os.getenv('STRIPE_API_KEY')

# Optional: Raise an error if the environment variable isn't set
if not stripe.api_key:
    raise ValueError("Stripe API key not found. Please set the STRIPE_API_KEY environment variable.")
