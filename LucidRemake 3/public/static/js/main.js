// Main JavaScript file for LucidQuant

document.addEventListener('DOMContentLoaded', function() {
    // Initialize smooth scrolling for anchor links
    initSmoothScrolling();
    
    // Initialize form handlers
    initFormHandlers();
    
    // Initialize animations
    initAnimations();
    
    // Initialize navbar scroll behavior
    initNavbarBehavior();
});

/**
 * Initialize smooth scrolling for anchor links
 */
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return; // Skip empty hash links
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                e.preventDefault();
                
                const headerOffset = 80; // Account for fixed navbar
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Initialize form handlers
 */
function initFormHandlers() {
    // Handle signup form submission
    const signupForm = document.querySelector('form[action*="signup"]');
    
    if (signupForm) {
        signupForm.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Show loading state
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';
            submitBtn.disabled = true;
            
            // Add timeout to prevent hanging
            setTimeout(() => {
                if (submitBtn.disabled) {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }
            }, 10000);
        });
    }
    
    // Email validation
    const emailInputs = document.querySelectorAll('input[type="email"]');
    
    emailInputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateEmail(this);
        });
        
        input.addEventListener('input', function() {
            // Clear any previous validation styling
            this.classList.remove('is-invalid', 'is-valid');
        });
    });
}

/**
 * Validate email input
 */
function validateEmail(input) {
    const email = input.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (email && !emailRegex.test(email)) {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
        
        // Add or update error message
        let errorMsg = input.parentNode.querySelector('.invalid-feedback');
        if (!errorMsg) {
            errorMsg = document.createElement('div');
            errorMsg.className = 'invalid-feedback';
            input.parentNode.appendChild(errorMsg);
        }
        errorMsg.textContent = 'Please enter a valid email address.';
    } else if (email) {
        input.classList.add('is-valid');
        input.classList.remove('is-invalid');
        
        // Remove error message
        const errorMsg = input.parentNode.querySelector('.invalid-feedback');
        if (errorMsg) {
            errorMsg.remove();
        }
    }
}

/**
 * Initialize scroll-based animations
 */
function initAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements that should animate on scroll
    const animateElements = document.querySelectorAll('.feature-card, .signal-card, .stat-item');
    
    animateElements.forEach(el => {
        // Set initial state
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        
        observer.observe(el);
    });
}

/**
 * Initialize navbar scroll behavior
 */
function initNavbarBehavior() {
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add background on scroll
        if (scrollTop > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Add CSS for scrolled state
    if (!document.querySelector('#navbar-scroll-style')) {
        const style = document.createElement('style');
        style.id = 'navbar-scroll-style';
        style.textContent = `
            .navbar.scrolled {
                background-color: rgba(31, 41, 55, 0.95) !important;
                backdrop-filter: blur(10px);
                box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
            }
        `;
        document.head.appendChild(style);
    }
}

/**
 * Utility function to show notifications
 */
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.cssText = 'top: 100px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

/**
 * Handle contact form submissions (if added later)
 */
function handleContactForm(form) {
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    
    // Basic validation
    if (!data.email || !data.message) {
        showNotification('Please fill in all required fields.', 'danger');
        return false;
    }
    
    if (!validateEmailString(data.email)) {
        showNotification('Please enter a valid email address.', 'danger');
        return false;
    }
    
    return true;
}

/**
 * Validate email string
 */
function validateEmailString(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Initialize particle background (optional enhancement)
 */
function initParticleBackground() {
    // This could be implemented later for additional visual appeal
    // Using libraries like particles.js or three.js
    console.log('Particle background can be implemented for enhanced visual appeal');
}

/**
 * Handle keyboard navigation
 */
document.addEventListener('keydown', function(e) {
    // Handle escape key to close modals or forms
    if (e.key === 'Escape') {
        const openModal = document.querySelector('.modal.show');
        if (openModal) {
            const modal = bootstrap.Modal.getInstance(openModal);
            if (modal) {
                modal.hide();
            }
        }
    }
});

/**
 * Performance optimization - lazy load images
 */
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback for older browsers
        images.forEach(img => {
            img.src = img.dataset.src;
        });
    }
}

// Initialize lazy loading when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLazyLoading);
} else {
    initLazyLoading();
}

/**
 * Initialize stock analyzer functionality
 */
function initializeStockAnalyzer() {
    const analyzeButtons = document.querySelectorAll('.analyze-btn');
    
    analyzeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const searchInput = this.parentElement.querySelector('.stock-search');
            const stockSymbol = searchInput.value.trim().toUpperCase();
            
            if (!stockSymbol) {
                alert('Please enter a stock symbol');
                return;
            }
            
            // Show loading state
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
            this.disabled = true;
            
            // Simulate analysis (in real implementation, this would call an API)
            setTimeout(() => {
                showAnalysisResult(stockSymbol, this);
                this.innerHTML = originalText;
                this.disabled = false;
            }, 2000);
        });
    });
}

/**
 * Show stock analysis result
 */
function showAnalysisResult(stockSymbol, button) {
    const resultContainer = button.parentElement.parentElement.querySelector('.analysis-result');
    
    if (resultContainer) {
        // Generate mock correlation data
        const correlations = ['Strong Positive', 'Moderate Positive', 'Weak Positive', 'Neutral', 'Weak Negative', 'Moderate Negative'];
        const correlation = correlations[Math.floor(Math.random() * correlations.length)];
        const score = (Math.random() * 100).toFixed(1);
        
        const descriptions = {
            'Strong Positive': `${stockSymbol} shows strong positive correlation with this indicator. When the indicator rises, ${stockSymbol} typically performs well.`,
            'Moderate Positive': `${stockSymbol} shows moderate positive correlation. This indicator can provide useful signals for ${stockSymbol} movements.`,
            'Weak Positive': `${stockSymbol} shows weak positive correlation. This indicator has limited predictive value for ${stockSymbol}.`,
            'Neutral': `${stockSymbol} shows neutral correlation. This indicator does not significantly influence ${stockSymbol} performance.`,
            'Weak Negative': `${stockSymbol} shows weak negative correlation. Inverse relationship with this indicator is minimal.`,
            'Moderate Negative': `${stockSymbol} shows moderate negative correlation. When this indicator rises, ${stockSymbol} may face headwinds.`
        };
        
        // Update result content
        resultContainer.querySelector('#stockSymbol').textContent = stockSymbol;
        resultContainer.querySelector('#correlationScore').textContent = `${score}% ${correlation}`;
        resultContainer.querySelector('#correlationDescription').textContent = descriptions[correlation];
        
        // Show result
        resultContainer.style.display = 'block';
        resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

/**
 * Initialize chart controls
 */
function initializeChartControls() {
    const timeButtons = document.querySelectorAll('.time-btn');
    
    timeButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            timeButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // In real implementation, this would update the chart data
            const period = this.dataset.period;
            console.log(`Chart updated to show ${period} data`);
        });
    });
}

// Initialize new functionality when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeStockAnalyzer();
    initializeChartControls();
});
