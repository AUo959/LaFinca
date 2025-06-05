# Create JavaScript functionality for the website
js_content = """// ==========================================================================
// Un Día en la Finca - Interactive Website Functionality
// ==========================================================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initNavigation();
    initContactForm();
    initScrollEffects();
    initPricingCalculator();
    
    console.log('Un Día en la Finca website loaded successfully!');
});

// ==========================================================================
// Navigation Functionality
// ==========================================================================

function initNavigation() {
    const navToggle = document.querySelector('.nav__toggle');
    const navMenu = document.querySelector('.nav__menu');
    const navLinks = document.querySelectorAll('.nav__link');
    
    // Mobile menu toggle
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });
    }
    
    // Close mobile menu when clicking on links
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            }
        });
    });
    
    // Smooth scrolling for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Header scroll effect
    window.addEventListener('scroll', function() {
        const header = document.querySelector('.header');
        if (window.scrollY > 100) {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
        } else {
            header.style.background = '#ffffff';
            header.style.backdropFilter = 'none';
        }
    });
}

// ==========================================================================
// Contact Form Functionality
// ==========================================================================

function initContactForm() {
    const contactForm = document.querySelector('.contact__form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(contactForm);
            const bookingData = {
                name: formData.get('name'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                guests: formData.get('guests'),
                checkin: formData.get('checkin'),
                nights: formData.get('nights'),
                dietary: formData.get('dietary'),
                message: formData.get('message')
            };
            
            // Basic validation
            if (!bookingData.name || !bookingData.email || !bookingData.guests) {
                showNotification('Please fill in all required fields.', 'error');
                return;
            }
            
            // Email validation
            if (!isValidEmail(bookingData.email)) {
                showNotification('Please enter a valid email address.', 'error');
                return;
            }
            
            // Calculate total cost
            const totalCost = calculateBookingCost(bookingData.guests, bookingData.nights);
            
            // Create booking summary
            const summary = createBookingSummary(bookingData, totalCost);
            
            // Show booking summary
            showBookingSummary(summary);
            
            // In a real implementation, you would send this data to your server
            console.log('Booking inquiry submitted:', bookingData);
            
            // Show success message
            showNotification('Booking inquiry submitted successfully! We will contact you soon.', 'success');
            
            // Reset form
            contactForm.reset();
        });
    }
}

function isValidEmail(email) {
    const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
    return emailRegex.test(email);
}

function calculateBookingCost(guests, nights) {
    const dailyRate = 297; // $297 per person per day
    const guestCount = parseInt(guests) || 1;
    const nightCount = parseInt(nights) || 1;
    
    return dailyRate * guestCount * nightCount;
}

function createBookingSummary(data, totalCost) {
    const guestCount = parseInt(data.guests) || 1;
    const nightCount = parseInt(data.nights) || 1;
    
    return {
        name: data.name,
        email: data.email,
        guests: guestCount,
        nights: nightCount,
        checkin: data.checkin,
        dailyRate: 297,
        subtotal: 297 * guestCount,
        totalNights: nightCount,
        totalCost: totalCost,
        dietary: data.dietary,
        message: data.message
    };
}

function showBookingSummary(summary) {
    const summaryHTML = `
        <div class="booking-summary-modal" id="bookingSummary">
            <div class="booking-summary-content">
                <div class="booking-summary-header">
                    <h3>Booking Summary</h3>
                    <button class="close-summary" onclick="closeBookingSummary()">&times;</button>
                </div>
                <div class="booking-summary-details">
                    <p><strong>Guest:</strong> ${summary.name}</p>
                    <p><strong>Email:</strong> ${summary.email}</p>
                    <p><strong>Number of Guests:</strong> ${summary.guests}</p>
                    <p><strong>Number of Nights:</strong> ${summary.nights}</p>
                    ${summary.checkin ? `<p><strong>Check-in Date:</strong> ${summary.checkin}</p>` : ''}
                    
                    <div class="cost-breakdown">
                        <h4>Cost Breakdown:</h4>
                        <p>Daily rate per person: $${summary.dailyRate}</p>
                        <p>Subtotal per day: $${summary.subtotal} (${summary.guests} guests)</p>
                        <p>Total nights: ${summary.nights}</p>
                        <p class="total-cost"><strong>Total Cost: $${summary.totalCost.toLocaleString()}</strong></p>
                    </div>
                    
                    ${summary.dietary ? `<p><strong>Dietary Restrictions:</strong> ${summary.dietary}</p>` : ''}
                    ${summary.message ? `<p><strong>Additional Message:</strong> ${summary.message}</p>` : ''}
                </div>
                <div class="booking-summary-footer">
                    <p><em>This is an inquiry only. Final confirmation and payment details will be provided via email.</em></p>
                </div>
            </div>
        </div>
    `;
    
    // Add styles if not already present
    if (!document.querySelector('#booking-summary-styles')) {
        const styles = document.createElement('style');
        styles.id = 'booking-summary-styles';
        styles.textContent = `
            .booking-summary-modal {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 10000;
            }
            .booking-summary-content {
                background: white;
                max-width: 500px;
                width: 90%;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            }
            .booking-summary-header {
                background: #004DB5;
                color: white;
                padding: 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .close-summary {
                background: none;
                border: none;
                color: white;
                font-size: 1.5rem;
                cursor: pointer;
                padding: 0;
                width: 30px;
                height: 30px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .booking-summary-details {
                padding: 1.5rem;
            }
            .cost-breakdown {
                background: #f5f5f5;
                padding: 1rem;
                border-radius: 8px;
                margin: 1rem 0;
            }
            .total-cost {
                font-size: 1.2rem;
                color: #CE1126;
                border-top: 2px solid #CE1126;
                padding-top: 0.5rem;
                margin-top: 0.5rem;
            }
            .booking-summary-footer {
                background: #f9f9f9;
                padding: 1rem;
                font-size: 0.9rem;
                color: #666;
            }
        `;
        document.head.appendChild(styles);
    }
    
    // Add modal to page
    document.body.insertAdjacentHTML('beforeend', summaryHTML);
}

function closeBookingSummary() {
    const modal = document.getElementById('bookingSummary');
    if (modal) {
        modal.remove();
    }
}

// ==========================================================================
// Pricing Calculator
// ==========================================================================

function initPricingCalculator() {
    const guestSelect = document.getElementById('guests');
    const nightsSelect = document.getElementById('nights');
    
    if (guestSelect && nightsSelect) {
        // Add event listeners for real-time calculation
        guestSelect.addEventListener('change', updatePricingPreview);
        nightsSelect.addEventListener('change', updatePricingPreview);
    }
}

function updatePricingPreview() {
    const guests = document.getElementById('guests').value;
    const nights = document.getElementById('nights').value;
    
    if (guests && nights) {
        const totalCost = calculateBookingCost(guests, nights);
        
        // Create or update pricing preview
        let pricingPreview = document.querySelector('.pricing-preview');
        if (!pricingPreview) {
            pricingPreview = document.createElement('div');
            pricingPreview.className = 'pricing-preview';
            pricingPreview.style.cssText = `
                background: #e3f2fd;
                border: 2px solid #004DB5;
                border-radius: 8px;
                padding: 1rem;
                margin-top: 1rem;
                text-align: center;
            `;
            
            const formGroups = document.querySelectorAll('.form__group');
            const lastFormGroup = formGroups[formGroups.length - 1];
            lastFormGroup.parentNode.insertBefore(pricingPreview, lastFormGroup.nextSibling);
        }
        
        pricingPreview.innerHTML = `
            <h4 style="color: #004DB5; margin-bottom: 0.5rem;">Estimated Total Cost</h4>
            <p style="font-size: 1.5rem; font-weight: bold; color: #CE1126; margin: 0;">
                $${totalCost.toLocaleString()}
            </p>
            <p style="font-size: 0.9rem; color: #666; margin: 0.5rem 0 0 0;">
                ${guests} guests × ${nights} nights × $297 per person/day
            </p>
        `;
    }
}

// ==========================================================================
// Scroll Effects and Animations
// ==========================================================================

function initScrollEffects() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.section__header, .feature, .package, .gallery__item, .attraction');
    animatedElements.forEach(el => {
        observer.observe(el);
    });
    
    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        
        if (hero) {
            const rate = scrolled * -0.5;
            hero.style.transform = `translateY(${rate}px)`;
        }
    });
}

// ==========================================================================
// Notification System
// ==========================================================================

function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#4CAF50' : type === 'error' ? '#f44336' : '#2196F3'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        z-index: 10001;
        max-width: 400px;
        font-family: 'Inter', sans-serif;
        animation: slideInRight 0.3s ease-out;
    `;
    
    notification.textContent = message;
    
    // Add animation styles if not present
    if (!document.querySelector('#notification-styles')) {
        const styles = document.createElement('style');
        styles.id = 'notification-styles';
        styles.textContent = `
            @keyframes slideInRight {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        `;
        document.head.appendChild(styles);
    }
    
    // Add to page
    document.body.appendChild(notification);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.style.animation = 'slideInRight 0.3s ease-out reverse';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }
    }, 5000);
}

// ==========================================================================
// Video Integration Helper
// ==========================================================================

function initVideoIntegration() {
    const videoPlaceholder = document.querySelector('.video__placeholder');
    
    if (videoPlaceholder) {
        videoPlaceholder.addEventListener('click', function() {
            // This function would handle video playback
            // For now, it shows instructions for video integration
            showNotification('To integrate your video, replace the placeholder with a proper video element or embed code.', 'info');
        });
    }
}

// ==========================================================================
// Utility Functions
// ==========================================================================

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

function formatDate(dateString) {
    if (!dateString) return '';
    
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// ==========================================================================
// Initialize additional features when DOM is ready
// ==========================================================================

document.addEventListener('DOMContentLoaded', function() {
    initVideoIntegration();
    
    // Add loading animation completion
    document.body.classList.add('loaded');
    
    // Log successful initialization
    console.log('All Un Día en la Finca features initialized successfully!');
});

// ==========================================================================
// Export functions for global access (if needed)
// ==========================================================================

window.UndiaEnLaFinca = {
    showNotification,
    calculateBookingCost,
    closeBookingSummary,
    formatCurrency,
    formatDate
};"""

print("JavaScript file content created successfully!")
print(f"File size: {len(js_content)} characters")