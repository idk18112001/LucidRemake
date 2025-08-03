from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import Indicator, Metric
from data_fetcher import DataFetcher

@app.route('/')
def index():
    """Main landing page for LucidQuant"""
    return render_template('index.html')

@app.route('/explore')
def explore():
    """Explore page for LucidQuant features"""
    return render_template('explore.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handle signup form submission"""
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            flash('Thank you for your interest! We\'ll be in touch soon.', 'success')
        else:
            flash('Please provide a valid email address.', 'error')
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html'), 404

@app.route('/indicators')
def indicators():
    """List all indicators"""
    # Get indicators from database, fallback to static data
    try:
        indicators = Indicator.query.all()
        if not indicators:
            raise Exception("No indicators in database")
    except:
        # Static fallback data
        indicators = [
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
            },
            {
                'name': 'Manufacturing PMI',
                'description': 'Manufacturing purchasing managers index',
                'category': 'Economic',
                'current_value': 52.1,
                'trend': 'up'
            },
            {
                'name': 'Google Search Trends',
                'description': 'Public interest and search volume for financial terms',
                'category': 'Behavioral',
                'current_value': 78.3,
                'trend': 'stable'
            }
        ]
    
    return render_template('indicators.html', indicators=indicators)

@app.route('/indicators/<int:indicator_id>')
def indicator_detail(indicator_id):
    """Show detailed view of a specific indicator"""
    # Static indicator data for demo
    indicators = [
        {
            'name': 'VIX Fear Index',
            'description': 'The VIX, or Volatility Index, measures the market\'s expectation of 30-day volatility. Often called the "fear gauge," it spikes during market uncertainty and drops during calm periods.',
            'category': 'Sentiment',
            'current_value': 22.5,
            'trend': 'stable'
        },
        {
            'name': 'Baltic Dry Index',
            'description': 'The Baltic Dry Index tracks the cost of shipping raw materials like coal, iron ore, and grain across major shipping routes, serving as a leading economic indicator.',
            'category': 'Economic',
            'current_value': 1245.0,
            'trend': 'up'
        },
        {
            'name': 'Insider Trading Patterns',
            'description': 'Tracks corporate insider buying and selling activity, providing insights into management confidence and potential future performance.',
            'category': 'Sentiment',
            'current_value': 89.2,
            'trend': 'up'
        },
        {
            'name': 'Consumer Confidence',
            'description': 'Measures consumer attitudes regarding economic conditions and their willingness to spend money.',
            'category': 'Economic',
            'current_value': 105.3,
            'trend': 'stable'
        },
        {
            'name': 'Manufacturing PMI',
            'description': 'The Manufacturing Purchasing Managers Index indicates the economic health of the manufacturing sector.',
            'category': 'Economic',
            'current_value': 52.1,
            'trend': 'up'
        },
        {
            'name': 'Google Search Trends',
            'description': 'Analyzes search volume for financial terms to gauge public interest and sentiment.',
            'category': 'Behavioral',
            'current_value': 78.3,
            'trend': 'stable'
        }
    ]
    
    if indicator_id > len(indicators):
        indicator = indicators[0]  # Default to first indicator
    else:
        indicator = indicators[indicator_id - 1]
    
    return render_template('indicator_detail.html', indicator=indicator)

@app.route('/metrics')
def metrics():
    """List all metrics"""
    # Static metrics data
    metrics = [
        {
            'name': 'Promoter Holding Change',
            'description': 'Changes in promoter shareholding patterns indicating management confidence and strategic decisions',
            'current_value': 65.4,
            'change_percentage': 2.1,
            'trend': 'up'
        },
        {
            'name': 'Bulk Dealings',
            'description': 'Large block transactions and institutional activity indicating major investor sentiment shifts',
            'current_value': 1247.0,
            'change_percentage': -1.8,
            'trend': 'down'
        },
        {
            'name': 'Insider Activity',
            'description': 'Corporate insider trading patterns and activity levels showing internal company perspectives',
            'current_value': 89.2,
            'change_percentage': 5.6,
            'trend': 'up'
        },
        {
            'name': 'Stock Trading Volume 50 Day Average',
            'description': '50-day average trading volume indicator showing short-term liquidity and market interest',
            'current_value': 1542.8,
            'change_percentage': 3.4,
            'trend': 'up'
        },
        {
            'name': 'Stock Trading Volume 200 Day Average',
            'description': '200-day average trading volume indicator showing long-term liquidity trends and market participation',
            'current_value': 1423.6,
            'change_percentage': 1.2,
            'trend': 'stable'
        }
    ]
    
    return render_template('metrics.html', metrics=metrics)

@app.route('/metrics/<int:metric_id>')
def metric_detail(metric_id):
    """Show detailed view of a specific metric"""
    # Static metrics data for detail view
    metrics = [
        {
            'name': 'Promoter Holding Change',
            'description': 'Changes in promoter shareholding patterns indicating management confidence and strategic decisions. Higher promoter holdings typically suggest confidence in the company\'s future prospects.',
            'current_value': 65.4,
            'change_percentage': 2.1,
            'trend': 'up'
        },
        {
            'name': 'Bulk Dealings',
            'description': 'Large block transactions and institutional activity indicating major investor sentiment shifts. High bulk dealing activity can signal significant institutional interest or divestment.',
            'current_value': 1247.0,
            'change_percentage': -1.8,
            'trend': 'down'
        },
        {
            'name': 'Insider Activity',
            'description': 'Corporate insider trading patterns and activity levels showing internal company perspectives. Insider buying often indicates positive internal outlook while selling may suggest profit-taking or personal liquidity needs.',
            'current_value': 89.2,
            'change_percentage': 5.6,
            'trend': 'up'
        },
        {
            'name': 'Stock Trading Volume 50 Day Average',
            'description': '50-day average trading volume indicator showing short-term liquidity and market interest. Higher volumes typically indicate increased market interest and better price discovery.',
            'current_value': 1542.8,
            'change_percentage': 3.4,
            'trend': 'up'
        },
        {
            'name': 'Stock Trading Volume 200 Day Average',
            'description': '200-day average trading volume indicator showing long-term liquidity trends and market participation. This metric helps identify sustained changes in investor interest over longer periods.',
            'current_value': 1423.6,
            'change_percentage': 1.2,
            'trend': 'stable'
        }
    ]
    
    if metric_id > len(metrics):
        metric = metrics[0]  # Default to first metric
    else:
        metric = metrics[metric_id - 1]
    
    return render_template('metric_detail.html', metric=metric)

@app.route('/admin/populate-data')
def populate_data():
    """Admin route to populate database with indicators and metrics"""
    try:
        fetcher = DataFetcher()
        fetcher.populate_database()
        flash('Database populated successfully!', 'success')
    except Exception as e:
        flash(f'Error populating database: {str(e)}', 'error')
    return redirect(url_for('explore'))

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('index.html'), 500
