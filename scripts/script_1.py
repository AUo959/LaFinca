# Create comprehensive CSS styling for the website
css_content = """/* ==========================================================================
   Un Día en la Finca - Professional Website Styles
   ========================================================================== */

/* CSS Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    /* Dominican Republic flag colors */
    --primary-blue: #004DB5;
    --primary-red: #CE1126;
    --primary-white: #FFFFFF;
    
    /* Additional colors */
    --dark-green: #2D5A2D;
    --light-green: #7CB342;
    --warm-brown: #8D6E63;
    --light-brown: #D7CCC8;
    --cream: #FFF8E1;
    --charcoal: #2C2C2C;
    --light-gray: #F5F5F5;
    --medium-gray: #9E9E9E;
    
    /* Typography */
    --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-weight-light: 300;
    --font-weight-normal: 400;
    --font-weight-medium: 500;
    --font-weight-semibold: 600;
    --font-weight-bold: 700;
    
    /* Spacing */
    --spacing-xs: 0.5rem;
    --spacing-sm: 1rem;
    --spacing-md: 2rem;
    --spacing-lg: 3rem;
    --spacing-xl: 4rem;
    --spacing-xxl: 6rem;
    
    /* Transitions */
    --transition: all 0.3s ease;
    
    /* Shadows */
    --shadow-light: 0 2px 8px rgba(0, 0, 0, 0.1);
    --shadow-medium: 0 4px 16px rgba(0, 0, 0, 0.15);
    --shadow-heavy: 0 8px 32px rgba(0, 0, 0, 0.2);
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-primary);
    line-height: 1.6;
    color: var(--charcoal);
    background-color: var(--primary-white);
}

img {
    max-width: 100%;
    height: auto;
}

/* ==========================================================================
   Layout Components
   ========================================================================== */

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--spacing-sm);
}

.section__header {
    text-align: center;
    margin-bottom: var(--spacing-xl);
}

.section__title {
    font-size: 2.5rem;
    font-weight: var(--font-weight-bold);
    color: var(--primary-blue);
    margin-bottom: var(--spacing-sm);
}

.section__subtitle {
    font-size: 1.2rem;
    color: var(--medium-gray);
    max-width: 600px;
    margin: 0 auto;
}

/* Buttons */
.btn {
    display: inline-block;
    padding: var(--spacing-sm) var(--spacing-md);
    font-family: var(--font-primary);
    font-weight: var(--font-weight-semibold);
    text-decoration: none;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: var(--transition);
    text-align: center;
    font-size: 1rem;
}

.btn--primary {
    background-color: var(--primary-red);
    color: var(--primary-white);
    box-shadow: var(--shadow-light);
}

.btn--primary:hover {
    background-color: #B50E20;
    transform: translateY(-2px);
    box-shadow: var(--shadow-medium);
}

/* ==========================================================================
   Header & Navigation
   ========================================================================== */

.header {
    background-color: var(--primary-white);
    box-shadow: var(--shadow-light);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
}

.nav {
    padding: var(--spacing-sm) 0;
}

.nav .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav__brand {
    text-align: left;
}

.nav__title {
    font-size: 1.8rem;
    font-weight: var(--font-weight-bold);
    color: var(--primary-blue);
    margin-bottom: 0.2rem;
}

.nav__subtitle {
    font-size: 0.9rem;
    color: var(--medium-gray);
    font-style: italic;
}

.nav__menu {
    display: flex;
    gap: var(--spacing-md);
}

.nav__link {
    text-decoration: none;
    color: var(--charcoal);
    font-weight: var(--font-weight-medium);
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: 4px;
    transition: var(--transition);
}

.nav__link:hover {
    color: var(--primary-red);
    background-color: var(--light-gray);
}

.nav__toggle {
    display: none;
    flex-direction: column;
    background: none;
    border: none;
    cursor: pointer;
    padding: var(--spacing-xs);
}

.nav__toggle span {
    width: 25px;
    height: 3px;
    background-color: var(--primary-blue);
    margin: 2px 0;
    transition: var(--transition);
}

/* ==========================================================================
   Hero Section
   ========================================================================== */

.hero {
    background: linear-gradient(135deg, var(--cream) 0%, var(--light-brown) 100%);
    padding: calc(80px + var(--spacing-xxl)) 0 var(--spacing-xxl) 0;
    text-align: center;
}

.hero__title {
    font-size: 3.5rem;
    font-weight: var(--font-weight-bold);
    color: var(--primary-blue);
    margin-bottom: var(--spacing-md);
    line-height: 1.2;
}

.hero__subtitle {
    font-size: 1.3rem;
    color: var(--charcoal);
    margin-bottom: var(--spacing-lg);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.hero__highlights {
    display: flex;
    justify-content: center;
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-lg);
    flex-wrap: wrap;
}

.highlight {
    display: flex;
    align-items: center;
    gap: var(--spacing-xs);
    background-color: var(--primary-white);
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: 25px;
    box-shadow: var(--shadow-light);
}

.highlight i {
    color: var(--primary-red);
    font-size: 1.2rem;
}

.hero__pricing {
    margin-bottom: var(--spacing-lg);
}

.hero__price {
    font-size: 4rem;
    font-weight: var(--font-weight-bold);
    color: var(--primary-red);
    display: block;
}

.hero__period {
    font-size: 1.2rem;
    color: var(--medium-gray);
    margin-right: var(--spacing-sm);
}

.hero__included {
    background-color: var(--dark-green);
    color: var(--primary-white);
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: var(--font-weight-semibold);
}

/* ==========================================================================
   About Section
   ========================================================================== */

.about {
    padding: var(--spacing-xxl) 0;
    background-color: var(--primary-white);
}

.about__content {
    max-width: 900px;
    margin: 0 auto;
}

.about__text h3 {
    font-size: 1.8rem;
    color: var(--primary-blue);
    margin-bottom: var(--spacing-sm);
}

.about__text p {
    margin-bottom: var(--spacing-md);
    font-size: 1.1rem;
    line-height: 1.7;
}

.about__features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-md);
    margin-top: var(--spacing-lg);
}

.feature {
    display: flex;
    gap: var(--spacing-sm);
    padding: var(--spacing-md);
    background-color: var(--light-gray);
    border-radius: 12px;
    border-left: 4px solid var(--primary-red);
}

.feature i {
    font-size: 1.5rem;
    color: var(--primary-blue);
    margin-top: 0.2rem;
}

.feature h4 {
    font-size: 1.2rem;
    color: var(--primary-blue);
    margin-bottom: var(--spacing-xs);
}

/* ==========================================================================
   Packages Section
   ========================================================================== */

.packages {
    padding: var(--spacing-xxl) 0;
    background-color: var(--light-gray);
}

.pricing__breakdown {
    background-color: var(--primary-white);
    padding: var(--spacing-lg);
    border-radius: 16px;
    box-shadow: var(--shadow-medium);
    margin-bottom: var(--spacing-xl);
}

.pricing__breakdown h3 {
    font-size: 2rem;
    color: var(--primary-blue);
    text-align: center;
    margin-bottom: var(--spacing-lg);
}

.breakdown__grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-lg);
}

.breakdown__category h4 {
    font-size: 1.3rem;
    color: var(--primary-red);
    margin-bottom: var(--spacing-sm);
    display: flex;
    align-items: center;
    gap: var(--spacing-xs);
}

.breakdown__category ul {
    list-style: none;
}

.breakdown__category li {
    display: flex;
    justify-content: space-between;
    padding: var(--spacing-xs) 0;
    border-bottom: 1px solid var(--light-gray);
}

.breakdown__category li span {
    font-weight: var(--font-weight-semibold);
    color: var(--primary-blue);
}

.packages__examples h3 {
    font-size: 2rem;
    color: var(--primary-blue);
    text-align: center;
    margin-bottom: var(--spacing-lg);
}

.packages__grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-md);
}

.package {
    background-color: var(--primary-white);
    padding: var(--spacing-lg);
    border-radius: 12px;
    box-shadow: var(--shadow-light);
    text-align: center;
    transition: var(--transition);
}

.package:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-medium);
}

.package h4 {
    font-size: 1.4rem;
    color: var(--primary-blue);
    margin-bottom: var(--spacing-sm);
}

.package__details {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
}

.package__price {
    font-size: 2rem;
    font-weight: var(--font-weight-bold);
    color: var(--primary-red);
}

/* ==========================================================================
   Experience Section
   ========================================================================== */

.experience {
    padding: var(--spacing-xxl) 0;
    background-color: var(--primary-white);
}

.video__container {
    text-align: center;
    margin-bottom: var(--spacing-xl);
}

.video__container h3 {
    font-size: 1.8rem;
    color: var(--primary-blue);
    margin-bottom: var(--spacing-md);
}

.video__placeholder {
    background-color: var(--light-gray);
    padding: var(--spacing-xl);
    border-radius: 16px;
    border: 2px dashed var(--medium-gray);
    max-width: 600px;
    margin: 0 auto;
}

.video__placeholder i {
    font-size: 4rem;
    color: var(--primary-red);
    margin-bottom: var(--spacing-sm);
}

.video__placeholder p {
    font-size: 1.1rem;
    color: var(--charcoal);
    margin-bottom: var(--spacing-xs);
}

.video__note {
    font-style: italic;
    color: var(--medium-gray);
    font-size: 0.9rem !important;
}

.experience__gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-lg);
}

.gallery__item {
    text-align: center;
    padding: var(--spacing-lg);
    background-color: var(--light-gray);
    border-radius: 12px;
}

.gallery__item i {
    font-size: 3rem;
    color: var(--primary-blue);
    margin-bottom: var(--spacing-sm);
}

.gallery__item h4 {
    font-size: 1.5rem;
    color: var(--primary-red);
    margin-bottom: var(--spacing-sm);
}

/* ==========================================================================
   Location Section
   ========================================================================== */

.location {
    padding: var(--spacing-xxl) 0;
    background-color: var(--light-gray);
}

.attractions__grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--spacing-md);
}

.attraction {
    background-color: var(--primary-white);
    padding: var(--spacing-lg);
    border-radius: 12px;
    box-shadow: var(--shadow-light);
    transition: var(--transition);
}

.attraction:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-medium);
}

.attraction h4 {
    font-size: 1.4rem;
    color: var(--primary-blue);
    margin-bottom: var(--spacing-sm);
}

.attraction p {
    line-height: 1.6;
}

/* ==========================================================================
   Contact Section
   ========================================================================== */

.contact {
    padding: var(--spacing-xxl) 0;
    background-color: var(--primary-white);
}

.contact__content {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: var(--spacing-xl);
    max-width: 1000px;
    margin: 0 auto;
}

.contact__form {
    background-color: var(--light-gray);
    padding: var(--spacing-lg);
    border-radius: 12px;
}

.form__row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--spacing-md);
    margin-bottom: var(--spacing-md);
}

.form__group {
    margin-bottom: var(--spacing-md);
}

.form__group label {
    display: block;
    font-weight: var(--font-weight-semibold);
    color: var(--charcoal);
    margin-bottom: var(--spacing-xs);
}

.form__group input,
.form__group select,
.form__group textarea {
    width: 100%;
    padding: var(--spacing-sm);
    border: 2px solid #E0E0E0;
    border-radius: 8px;
    font-family: var(--font-primary);
    font-size: 1rem;
    transition: var(--transition);
}

.form__group input:focus,
.form__group select:focus,
.form__group textarea:focus {
    outline: none;
    border-color: var(--primary-blue);
    box-shadow: 0 0 0 3px rgba(0, 77, 181, 0.1);
}

.contact__info {
    background-color: var(--dark-green);
    color: var(--primary-white);
    padding: var(--spacing-lg);
    border-radius: 12px;
    height: fit-content;
}

.contact__info h3 {
    font-size: 1.5rem;
    margin-bottom: var(--spacing-md);
}

.contact__details p {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    margin-bottom: var(--spacing-sm);
}

.contact__details i {
    color: var(--light-green);
}

/* ==========================================================================
   Footer
   ========================================================================== */

.footer {
    background-color: var(--charcoal);
    color: var(--primary-white);
    padding: var(--spacing-xl) 0 var(--spacing-md) 0;
}

.footer__content {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: var(--spacing-xl);
    margin-bottom: var(--spacing-lg);
}

.footer__brand h3 {
    font-size: 1.8rem;
    color: var(--primary-white);
    margin-bottom: var(--spacing-xs);
}

.footer__disclaimers h4 {
    color: var(--primary-red);
    margin-bottom: var(--spacing-sm);
}

.footer__disclaimers ul {
    list-style: none;
}

.footer__disclaimers li {
    font-size: 0.9rem;
    line-height: 1.5;
    margin-bottom: var(--spacing-xs);
    padding-left: var(--spacing-sm);
    position: relative;
}

.footer__disclaimers li:before {
    content: "•";
    color: var(--primary-red);
    position: absolute;
    left: 0;
}

.footer__bottom {
    border-top: 1px solid #444;
    padding-top: var(--spacing-md);
    text-align: center;
    font-size: 0.9rem;
    color: var(--medium-gray);
}

/* ==========================================================================
   Responsive Design
   ========================================================================== */

@media (max-width: 768px) {
    .nav__menu {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background-color: var(--primary-white);
        flex-direction: column;
        padding: var(--spacing-md);
        box-shadow: var(--shadow-medium);
    }
    
    .nav__menu.active {
        display: flex;
    }
    
    .nav__toggle {
        display: flex;
    }
    
    .hero__title {
        font-size: 2.5rem;
    }
    
    .hero__highlights {
        flex-direction: column;
        align-items: center;
    }
    
    .section__title {
        font-size: 2rem;
    }
    
    .breakdown__grid {
        grid-template-columns: 1fr;
    }
    
    .form__row {
        grid-template-columns: 1fr;
    }
    
    .contact__content {
        grid-template-columns: 1fr;
    }
    
    .footer__content {
        grid-template-columns: 1fr;
        text-align: center;
    }
}

@media (max-width: 480px) {
    .hero__title {
        font-size: 2rem;
    }
    
    .hero__price {
        font-size: 3rem;
    }
    
    .packages__grid {
        grid-template-columns: 1fr;
    }
    
    .experience__gallery {
        grid-template-columns: 1fr;
    }
    
    .attractions__grid {
        grid-template-columns: 1fr;
    }
}

/* ==========================================================================
   Animation and Scroll Effects
   ========================================================================== */

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in {
    animation: fadeInUp 0.6s ease-out;
}

/* Smooth scroll padding for fixed header */
html {
    scroll-padding-top: 80px;
}"""

print("CSS file content created successfully!")
print(f"File size: {len(css_content)} characters")