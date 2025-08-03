import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__, 
           template_folder='templates', 
           static_folder='../public/static',
           static_url_path='/static')
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return {'status': 'ok', 'message': 'LucidQuant is running!'}

@app.route('/explore')
def explore():
    # For Vercel, we'll use static data since database setup is complex
    static_indicators = [
        {
            'name': 'VIX Fear Index',
            'description': 'Market volatility and fear sentiment analysis',
            'category': 'Sentiment',
            'current_value': 22.5,
            'trend': 'stable'
        },
        {
            'name': 'Baltic Dry Index',
            'description': 'Global shipping rates as economic indicator',
            'category': 'Economic',
            'current_value': 1245.0,
            'trend': 'up'
        },
        {
            'name': 'Insider Trading Patterns',
            'description': 'Corporate insider buying and selling activity',
            'category': 'Sentiment',
            'current_value': 89.2,
            'trend': 'up'
        },
        {
            'name': 'Consumer Confidence',
            'description': 'Consumer confidence index and sentiment',
            'category': 'Economic',
            'current_value': 105.3,
            'trend': 'stable'
        }
    ]
    
    static_metrics = [
        {
            'name': 'Promoter Holding Change',
            'description': 'Changes in promoter shareholding patterns',
            'current_value': 65.4,
            'change_percentage': 2.1,
            'trend': 'up'
        },
        {
            'name': 'Bulk Dealings',
            'description': 'Large block transactions and institutional activity',
            'current_value': 1247.0,
            'change_percentage': -1.8,
            'trend': 'down'
        },
        {
            'name': 'Insider Activity',
            'description': 'Corporate insider trading patterns and activity',
            'current_value': 89.2,
            'change_percentage': 5.6,
            'trend': 'up'
        },
        {
            'name': 'Stock Trading Volume 50 Day Average',
            'description': '50-day average trading volume indicator',
            'current_value': 1542.8,
            'change_percentage': 3.4,
            'trend': 'up'
        },
        {
            'name': 'Stock Trading Volume 200 Day Average',
            'description': '200-day average trading volume indicator',
            'current_value': 1423.6,
            'change_percentage': 1.2,
            'trend': 'stable'
        }
    ]
    
    return render_template('explore.html', indicators=static_indicators, metrics=static_metrics)

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    
    if not email:
        flash('Please provide an email address.', 'error')
        return redirect(url_for('index'))
    
    # Basic email validation
    if '@' not in email or '.' not in email:
        flash('Please provide a valid email address.', 'error')
        return redirect(url_for('index'))
    
    # Here you would typically save to database
    # For now, just show success message
    flash(f'Thank you for signing up! We\'ll be in touch at {email}', 'success')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    # Log the error for debugging
    app.logger.error(f'404 error: {error}')
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    # Log the error for debugging  
    app.logger.error(f'500 error: {error}')
    return render_template('index.html'), 500

# For Vercel, we need to export the app as 'app'
# Vercel will automatically use the 'app' variable

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)