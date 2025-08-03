# Overview

LucidQuant is a Flask-based web application that serves as a landing page for an alternative investment signals platform. The application focuses on presenting unconventional data sources and investment opportunities that traditional analysis platforms might miss. It features a modern, responsive design showcasing services like satellite intelligence, social sentiment analysis, and other alternative indicators for investment decision-making.

**Recent Update**: The application has been restructured for Vercel deployment using serverless functions while maintaining all original functionality.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Template Engine**: Jinja2 templating with Flask's built-in template rendering
- **CSS Framework**: Bootstrap 5.3.0 for responsive design and UI components
- **Icon Library**: Font Awesome 6.4.0 for consistent iconography
- **Typography**: Google Fonts (Inter) for modern, readable typography
- **JavaScript**: Vanilla JavaScript for smooth scrolling, form handling, and basic animations
- **Design Pattern**: Mobile-first responsive design with custom CSS variables for consistent theming

## Backend Architecture
- **Web Framework**: Flask with modular route organization
- **Application Structure**: 
  - `app.py` - Main application factory and configuration (original)
  - `api/index.py` - Vercel serverless function entry point
  - `vercel.json` - Vercel deployment configuration
  - `main.py` - Entry point for deployment environments
- **Session Management**: Flask sessions with configurable secret key
- **Error Handling**: Custom 404 and 500 error handlers that gracefully redirect to the main page
- **Logging**: Built-in Python logging configured for debugging
- **Deployment**: Configured for both Replit and Vercel deployment options

## Routing Structure
- **Landing Page** (`/`) - Main hero section with features overview
- **Explore Page** (`/explore`) - Detailed showcase of signal categories and alternative data sources
- **Signup Endpoint** (`/signup`) - POST handler for email collection with flash messaging
- **Error Handling** - Graceful fallback to main page for unhandled routes

## Static Asset Organization
- **CSS**: Custom styles in `/static/css/style.css` with CSS custom properties for theming
- **JavaScript**: Main functionality in `/static/js/main.js` with modular function organization
- **Design System**: Consistent color scheme and typography using CSS variables

# External Dependencies

## Frontend Libraries
- **Bootstrap 5.3.0** - CSS framework via CDN for responsive UI components
- **Font Awesome 6.4.0** - Icon library via CDN for consistent iconography
- **Google Fonts** - Inter font family for modern typography

## Backend Dependencies
- **Flask** - Core web framework for Python
- **Standard Library** - Uses Python's built-in logging and os modules

## Development Environment
- **Debug Mode** - Enabled for development with Flask's built-in debugger
- **Environment Variables** - SESSION_SECRET for production security configuration
- **Host Configuration** - Configured to run on 0.0.0.0:5000 for container compatibility

## Notable Architectural Decisions
- **No Database Layer**: Currently operates as a static informational site with simple form handling
- **Minimal Dependencies**: Deliberately lightweight with only essential Flask components
- **CDN-Based Assets**: External libraries loaded via CDN to reduce bundle size and improve loading performance
- **Modular JavaScript**: Client-side code organized into discrete functions for maintainability