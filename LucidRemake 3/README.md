# LucidQuant - Alternative Investment Signals Platform

A sophisticated Flask-based web application showcasing alternative investment signals and unconventional market analysis with a dark navy theme and teal accents.

## Features

- **Dark Navy Theme**: Modern design with teal accent colors
- **Scroll Hijacking**: Smooth layered scroll effects for offerings section
- **Responsive Design**: Mobile-first approach with elegant typography
- **Sign-up Modal**: Interactive email collection functionality
- **Split-screen Explore**: Indicators and Metrics sections

## Deployment Options

### Option 1: Vercel Deployment (Recommended for production)

1. **Prerequisites**: 
   - Vercel account
   - Git repository connected to Vercel

2. **Deploy to Vercel**:
   ```bash
   # Clone/upload this repository to your Git provider (GitHub, GitLab, etc.)
   # Connect the repository to Vercel
   # Vercel will automatically detect the vercel.json configuration
   ```

3. **Files for Vercel**:
   - `vercel.json` - Deployment configuration
   - `api/index.py` - Serverless function entry point
   - `api/templates/` - Template files
   - `public/static/` - Static assets (CSS, JS)

### Option 2: Replit Deployment

1. **Use Replit's deployment feature**:
   - Click the "Deploy" button in Replit
   - Follow the deployment wizard
   - Uses the existing Flask structure

## File Structure

```
├── api/
│   ├── index.py          # Vercel serverless function
│   └── templates/        # Template files for Vercel
├── public/
│   └── static/           # Static assets for Vercel
├── templates/            # Original template files
├── static/               # Original static files
├── app.py               # Original Flask app
├── routes.py            # Route handlers
├── main.py              # Entry point
├── vercel.json          # Vercel configuration
└── replit.md            # Project documentation
```

## Local Development

```bash
# Install dependencies (handled automatically in Replit)
pip install flask email-validator gunicorn

# Run the application
python main.py
# or
python app.py
```

## Environment Variables

- `SESSION_SECRET`: Secret key for Flask sessions (set automatically in production)

## Design Elements

- **Typography**: Inter font family with light weights (200-400)
- **Colors**: Navy (#0a0e27) background with teal (#14b8a6) accents
- **Animations**: CSS-based fade-ins and scroll-triggered effects
- **Layout**: Sticky positioning for scroll hijacking effects

## Browser Support

- Modern browsers with CSS custom properties support
- Responsive design for mobile and desktop
- Smooth scrolling and backdrop-filter effects