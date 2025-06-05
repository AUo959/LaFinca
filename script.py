# Create a comprehensive HTML structure for Un Día en la Finca website
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Un Día en la Finca - Authentic Dominican Countryside Experience</title>
    <meta name="description" content="Experience authentic Dominican countryside living in Mata Caliche. All-inclusive agritourism with local hosts, traditional meals, and genuine rural culture.">
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <!-- Header & Navigation -->
    <header class="header">
        <nav class="nav">
            <div class="container">
                <div class="nav__brand">
                    <h1 class="nav__title">Un Día en la Finca</h1>
                    <p class="nav__subtitle">Authentic Dominican Countryside</p>
                </div>
                <button class="nav__toggle" aria-label="Toggle navigation">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <div class="nav__menu">
                    <a href="#home" class="nav__link">Home</a>
                    <a href="#about" class="nav__link">About</a>
                    <a href="#packages" class="nav__link">Packages</a>
                    <a href="#experience" class="nav__link">Experience</a>
                    <a href="#location" class="nav__link">Location</a>
                    <a href="#contact" class="nav__link">Contact</a>
                </div>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="container">
            <div class="hero__content">
                <h1 class="hero__title">Experience Authentic Dominican Countryside Living</h1>
                <p class="hero__subtitle">Immerse yourself in genuine local hospitality away from resorts. Stay with a local family in Mata Caliche and discover the real Dominican Republic.</p>
                <div class="hero__highlights">
                    <div class="highlight">
                        <i class="fas fa-home"></i>
                        <span>Real Countryside Living</span>
                    </div>
                    <div class="highlight">
                        <i class="fas fa-utensils"></i>
                        <span>Traditional Dominican Meals</span>
                    </div>
                    <div class="highlight">
                        <i class="fas fa-car"></i>
                        <span>Car Rental Included</span>
                    </div>
                </div>
                <div class="hero__pricing">
                    <span class="hero__price">$297</span>
                    <span class="hero__period">per person/day</span>
                    <span class="hero__included">All-inclusive</span>
                </div>
                <a href="#contact" class="btn btn--primary">Book Your Stay</a>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">About Un Día en la Finca</h2>
                <p class="section__subtitle">This is NOT a resort - it's authentic Dominican countryside life</p>
            </div>
            <div class="about__content">
                <div class="about__text">
                    <h3>Authentic Experience, Not Luxury</h3>
                    <p>Un Día en la Finca offers a genuine countryside experience in Mata Caliche, near San José de los Llanos, San Pedro de Macorís. We provide real Dominican rural hospitality - no pretense, no luxury amenities, just authentic connections with local culture and genuine warmth.</p>
                    
                    <h3>Historical Significance</h3>
                    <p>San José de los Llanos holds unique significance in Dominican history as the location where Vicente Celestino Duarte first declared independence from Haitian rule on February 26, 1844 - one day before the famous declaration in Santo Domingo. This makes it the site of the very first Independence Day in Dominican Republic history.</p>
                    
                    <div class="about__features">
                        <div class="feature">
                            <i class="fas fa-bed"></i>
                            <div>
                                <h4>Comfortable Accommodations</h4>
                                <p>2 guest rooms with private bathrooms and AC</p>
                            </div>
                        </div>
                        <div class="feature">
                            <i class="fas fa-swimming-pool"></i>
                            <div>
                                <h4>Rural Amenities</h4>
                                <p>Swimming pool, large deck, separate kitchen/bar</p>
                            </div>
                        </div>
                        <div class="feature">
                            <i class="fas fa-leaf"></i>
                            <div>
                                <h4>Fresh from the Land</h4>
                                <p>Fruit trees: coconut, orange, avocado</p>
                            </div>
                        </div>
                        <div class="feature">
                            <i class="fas fa-heart"></i>
                            <div>
                                <h4>Local Hospitality</h4>
                                <p>Hosted by caring local family</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Packages Section -->
    <section id="packages" class="packages">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">All-Inclusive Packages</h2>
                <p class="section__subtitle">Transparent pricing - everything included</p>
            </div>
            
            <!-- Detailed Breakdown -->
            <div class="pricing__breakdown">
                <h3>What's Included ($297 per person/day)</h3>
                <div class="breakdown__grid">
                    <div class="breakdown__category">
                        <h4><i class="fas fa-utensils"></i> Meals</h4>
                        <ul>
                            <li>Breakfast <span>$8</span></li>
                            <li>Lunch <span>$10</span></li>
                            <li>Dinner <span>$12</span></li>
                            <li>À la carte dinner <span>$25</span></li>
                            <li>Platter lunch (additional) <span>$35</span></li>
                        </ul>
                    </div>
                    <div class="breakdown__category">
                        <h4><i class="fas fa-glass-cheers"></i> Beverages</h4>
                        <ul>
                            <li>Coffee (4 servings) <span>$8</span></li>
                            <li>Water (7 servings) <span>$14</span></li>
                            <li>Juice (3 servings) <span>$9</span></li>
                            <li>Smoothies (4 servings) <span>$16</span></li>
                            <li>Beer (4 servings) <span>$12</span></li>
                            <li>Rum (6 servings) <span>$18</span></li>
                            <li>Margaritas (6 servings) <span>$18</span></li>
                        </ul>
                    </div>
                    <div class="breakdown__category">
                        <h4><i class="fas fa-concierge-bell"></i> Services</h4>
                        <ul>
                            <li>Accommodation <span>$85</span></li>
                            <li>Rental car <span>$27</span></li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Package Examples -->
            <div class="packages__examples">
                <h3>Package Examples</h3>
                <div class="packages__grid">
                    <div class="package">
                        <h4>Solo Traveler</h4>
                        <div class="package__details">
                            <span>1 person, 1 day</span>
                            <span class="package__price">$297</span>
                        </div>
                    </div>
                    <div class="package">
                        <h4>Extended Solo Stay</h4>
                        <div class="package__details">
                            <span>1 person, 4 days</span>
                            <span class="package__price">$1,188</span>
                        </div>
                    </div>
                    <div class="package">
                        <h4>Group Experience</h4>
                        <div class="package__details">
                            <span>4 people, 1 day</span>
                            <span class="package__price">$1,188</span>
                        </div>
                    </div>
                    <div class="package">
                        <h4>Group Retreat</h4>
                        <div class="package__details">
                            <span>4 people, 4 days</span>
                            <span class="package__price">$4,752</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="experience">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Your Countryside Experience</h2>
                <p class="section__subtitle">See what a day at our finca looks like</p>
            </div>
            
            <!-- Video Integration -->
            <div class="video__container">
                <h3>Take a Virtual Tour</h3>
                <div class="video__placeholder">
                    <i class="fas fa-play-circle"></i>
                    <p>Video: ScreenRecording_05-05-2025-13-28-39_1.mov</p>
                    <p class="video__note">Upload your video file to see the authentic finca experience</p>
                </div>
            </div>
            
            <!-- Experience Gallery -->
            <div class="experience__gallery">
                <div class="gallery__item">
                    <i class="fas fa-sun"></i>
                    <h4>Morning</h4>
                    <p>Wake to roosters crowing and birds singing. Enjoy fresh fruit from our trees and traditional Dominican breakfast.</p>
                </div>
                <div class="gallery__item">
                    <i class="fas fa-utensils"></i>
                    <h4>Afternoon</h4>
                    <p>Learn traditional cooking, relax by the pool, or explore the countryside. All meals prepared with local ingredients.</p>
                </div>
                <div class="gallery__item">
                    <i class="fas fa-moon"></i>
                    <h4>Evening</h4>
                    <p>Share stories with your hosts, enjoy local rum or margaritas, and experience the peaceful countryside night.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Location Section -->
    <section id="location" class="location">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Location & Nearby Attractions</h2>
                <p class="section__subtitle">Mata Caliche, San José de los Llanos, San Pedro de Macorís</p>
            </div>
            
            <div class="attractions__grid">
                <div class="attraction">
                    <h4>Boca Chica Beach</h4>
                    <p>Famous for its turquoise, shallow waters and lively local atmosphere - perfect for swimming and enjoying fresh seafood.</p>
                </div>
                <div class="attraction">
                    <h4>Juan Dolio</h4>
                    <p>A peaceful, family-friendly beach with local restaurants and a relaxed atmosphere.</p>
                </div>
                <div class="attraction">
                    <h4>San Pedro de Macorís</h4>
                    <p>Historic city featuring the Malecón waterfront promenade, Central Park, cathedral, and unique cultural attractions.</p>
                </div>
                <div class="attraction">
                    <h4>Cueva de las Maravillas</h4>
                    <p>Impressive cave system with fascinating geology and historical significance.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Book Your Authentic Experience</h2>
                <p class="section__subtitle">Ready to experience real Dominican countryside living?</p>
            </div>
            
            <div class="contact__content">
                <form class="contact__form">
                    <div class="form__row">
                        <div class="form__group">
                            <label for="name">Full Name *</label>
                            <input type="text" id="name" name="name" required>
                        </div>
                        <div class="form__group">
                            <label for="email">Email *</label>
                            <input type="email" id="email" name="email" required>
                        </div>
                    </div>
                    <div class="form__row">
                        <div class="form__group">
                            <label for="phone">Phone Number</label>
                            <input type="tel" id="phone" name="phone">
                        </div>
                        <div class="form__group">
                            <label for="guests">Number of Guests *</label>
                            <select id="guests" name="guests" required>
                                <option value="">Select number of guests</option>
                                <option value="1">1 person</option>
                                <option value="2">2 people</option>
                                <option value="3">3 people</option>
                                <option value="4">4 people</option>
                                <option value="5">5 people</option>
                                <option value="6">6 people</option>
                                <option value="7">7 people</option>
                            </select>
                        </div>
                    </div>
                    <div class="form__row">
                        <div class="form__group">
                            <label for="checkin">Preferred Check-in Date</label>
                            <input type="date" id="checkin" name="checkin">
                        </div>
                        <div class="form__group">
                            <label for="nights">Number of Nights</label>
                            <select id="nights" name="nights">
                                <option value="">Select nights</option>
                                <option value="1">1 night</option>
                                <option value="2">2 nights</option>
                                <option value="3">3 nights</option>
                                <option value="4">4 nights</option>
                                <option value="5">5 nights</option>
                                <option value="6">6 nights</option>
                                <option value="7">7 nights</option>
                            </select>
                        </div>
                    </div>
                    <div class="form__group">
                        <label for="dietary">Dietary Restrictions or Special Requests</label>
                        <textarea id="dietary" name="dietary" rows="3"></textarea>
                    </div>
                    <div class="form__group">
                        <label for="message">Additional Message</label>
                        <textarea id="message" name="message" rows="4" placeholder="Tell us about your interests and what you hope to experience..."></textarea>
                    </div>
                    <button type="submit" class="btn btn--primary">Send Booking Inquiry</button>
                </form>
                
                <div class="contact__info">
                    <h3>Contact Information</h3>
                    <div class="contact__details">
                        <p><i class="fas fa-map-marker-alt"></i> Mata Caliche, San José de los Llanos, San Pedro de Macorís, Dominican Republic</p>
                        <p><i class="fas fa-envelope"></i> [Your Email Here]</p>
                        <p><i class="fas fa-phone"></i> [Your Phone Here]</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer__content">
                <div class="footer__brand">
                    <h3>Un Día en la Finca</h3>
                    <p>Authentic Dominican Countryside Experience</p>
                </div>
                
                <div class="footer__disclaimers">
                    <h4>Important Notes</h4>
                    <ul>
                        <li>Power outages may occur as part of authentic countryside experience; fans and natural breezes provided as backup</li>
                        <li>This is not a resort - expect genuine, rustic countryside living</li>
                        <li>Rural setting includes natural wildlife and mosquitoes</li>
                        <li>Un Día en la Finca is not responsible for injuries or incidents during off-property activities (beach, river, car rental)</li>
                        <li>Guests assume personal responsibility for their safety and for supervising minors</li>
                        <li>Third-party services are solely between guest and provider - not covered by our liability</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer__bottom">
                <p>&copy; 2025 Un Día en la Finca. All rights reserved.</p>
                <p>Website developed as part of Perplexity Labs project</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>"""

print("HTML file content created successfully!")
print(f"File size: {len(html_content)} characters")