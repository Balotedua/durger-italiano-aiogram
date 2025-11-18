def generate_physical_health_page():
    """Physical Health Hub - Ultra Premium Nero & Oro"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-light: #F4E5B2;
            --gold-dark: #9B7F1B;
            --black: #0A0A0A;
            --black-light: #1A1A1A;
            --black-lighter: #2A2A2A;
            --white: #FFFFFF;
        }

        body { background: var(--black) !important; }
        .bg-gradient {
            background: radial-gradient(circle at 20% 50%, rgba(212,175,55,0.15) 0%, transparent 50%),
                        radial-gradient(circle at 80% 50%, rgba(212,175,55,0.1) 0%, transparent 50%) !important;
        }

        /* Header */
        .premium-header {
            text-align: center;
            padding: 60px 20px 40px;
            position: relative;
        }

        .logo-icon {
            font-size: 72px;
            filter: drop-shadow(0 8px 24px rgba(212,175,55,0.4));
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-12px); }
        }

        .app-name {
            font-family: 'Playfair Display', serif;
            font-size: 42px;
            font-weight: 900;
            background: linear-gradient(135deg, var(--gold-light), var(--gold), var(--gold-dark));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -1px;
            margin: 16px 0 8px;
            text-shadow: 0 0 40px rgba(212,175,55,0.3);
        }

        .tagline {
            font-family: 'Inter', sans-serif;
            font-size: 15px;
            font-weight: 500;
            color: var(--gold-light);
            letter-spacing: 4px;
            text-transform: uppercase;
            opacity: 0.9;
        }

        .divider {
            width: 80px;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--gold), transparent);
            margin: 32px auto;
        }

        /* Cards */
        .cards-container {
            max-width: 500px;
            margin: 0 auto;
            padding: 0 20px 40px;
        }

        .premium-card {
            position: relative;
            background: var(--black-light);
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 24px;
            padding: 32px 28px;
            margin-bottom: 20px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            text-decoration: none;
            display: block;
            overflow: hidden;
        }

        .premium-card::before {
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(212,175,55,0.1), transparent);
            transition: left 0.6s ease;
        }

        .premium-card:active::before { left: 100%; }

        .premium-card::after {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 24px;
            padding: 1px;
            background: linear-gradient(135deg, var(--gold), transparent, var(--gold));
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            opacity: 0;
            transition: opacity 0.4s;
        }

        .premium-card:active {
            transform: translateY(-4px) scale(1.02);
            border-color: rgba(212,175,55,0.5);
            box-shadow: 0 20px 60px rgba(212,175,55,0.3);
        }

        .premium-card:active::after { opacity: 1; }

        .card-header { display: flex; align-items: center; gap: 20px; margin-bottom: 16px; }
        .card-icon-container {
            width: 64px; height: 64px;
            background: linear-gradient(135deg, rgba(212,175,55,0.15), rgba(212,175,55,0.05));
            border: 1px solid rgba(212,175,55,0.3);
            border-radius: 18px;
            display: flex; align-items: center; justify-content: center;
            transition: all 0.4s ease;
        }

        .premium-card:active .card-icon-container {
            transform: scale(1.1) rotate(5deg);
            background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.15));
        }

        .card-icon { font-size: 36px; filter: drop-shadow(0 4px 12px rgba(212,175,55,0.3)); }
        .card-title {
            font-family: 'Playfair Display', serif;
            font-size: 24px;
            font-weight: 700;
            color: var(--gold-light);
            margin-bottom: 4px;
        }

        .card-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            font-weight: 500;
            color: rgba(212,175,55,0.7);
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }

        .card-description {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: rgba(255,255,255,0.7);
            line-height: 1.6;
            margin-top: 12px;
        }

        .card-arrow {
            position: absolute;
            right: 24px; top: 50%;
            transform: translateY(-50%);
            font-size: 24px;
            color: var(--gold);
            opacity: 0.5;
            transition: all 0.4s ease;
        }

        .premium-card:active .card-arrow {
            opacity: 1;
            transform: translateY(-50%) translateX(8px);
        }

        /* Particles */
        .gold-particle {
            position: fixed;
            width: 3px; height: 3px;
            background: var(--gold);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            opacity: 0;
            animation: particle-float linear infinite;
        }

        @keyframes particle-float {
            0% { opacity: 0; transform: translateY(100vh) scale(0); }
            10% { opacity: 0.8; }
            90% { opacity: 0.8; }
            100% { opacity: 0; transform: translateY(-20vh) scale(1); }
        }
    </style>

    <div class="premium-header">
        <div class="logo-icon">💪</div>
        <h1 class="app-name">PHYSICAL WELLNESS</h1>
        <div class="tagline">IL TUO CORPO È UN TEMPIO</div>
        <div class="divider"></div>
    </div>

    <div class="cards-container">

        <a href="/workout" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container"><div class="card-icon">🏋️</div></div>
                <div class="card-content">
                    <div class="card-title">Workout Planner</div>
                    <div class="card-subtitle">Programmi Personalizzati</div>
                </div>
            </div>
            <div class="card-description">Allenamenti su misura per i tuoi obiettivi: forza, resistenza, ipertrofia o dimagrimento</div>
            <div class="card-arrow">→</div>
        </a>

        <a href="/nutrition" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container"><div class="card-icon">🥗</div></div>
                <div class="card-content">
                    <div class="card-title">Nutrition Coach</div>
                    <div class="card-subtitle">Piani Alimentari Elite</div>
                </div>
            </div>
            <div class="card-description">Diete personalizzate, tracking macro, ricette gourmet e integrazione avanzata</div>
            <div class="card-arrow">→</div>
        </a>

        <a href="/tracking" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container"><div class="card-icon">📊</div></div>
                <div class="card-content">
                    <div class="card-title">Progress Tracker</div>
                    <div class="card-subtitle">Analytics & Insights</div>
                </div>
            </div>
            <div class="card-description">Monitora peso, misure, foto prima/dopo, forza e performance con grafici premium</div>
            <div class="card-arrow">→</div>
        </a>

        <a href="/recovery" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container"><div class="card-icon">🧘</div></div>
                <div class="card-content">
                    <div class="card-title">Recovery & Mobility</div>
                    <div class="card-subtitle">Rigenerazione Totale</div>
                </div>
            </div>
            <div class="card-description">Stretching dinamico, foam rolling, sonno ottimizzato e tecniche di recupero attivo</div>
            <div class="card-arrow">→</div>
        </a>

        <a href="/challenges" class="premium-card">
            <div class="card-header">
                <div class="card-icon-container"><div class="card-icon">🔥</div></div>
                <div class="card-content">
                    <div class="card-title">90-Day Challenges</div>
                    <div class="card-subtitle">Trasformazioni Estreme</div>
                </div>
            </div>
            <div class="card-description">Programmi intensivi di 90 giorni con coaching dedicato e premi esclusivi</div>
            <div class="card-arrow">→</div>
        </a>

    </div>

    <script>
        // Particelle oro
        function createGoldParticles() {
            for (let i = 0; i < 18; i++) {
                const p = document.createElement('div');
                p.className = 'gold-particle';
                p.style.left = Math.random() * 100 + '%';
                p.style.animationDuration = (Math.random() * 10 + 8) + 's';
                p.style.animationDelay = Math.random() * 5 + 's';
                document.body.appendChild(p);
            }
        }
        createGoldParticles();

        // Haptic feedback
        document.querySelectorAll('.premium-card').forEach(card => {
            card.addEventListener('click', function(e) {
                e.preventDefault();
                Telegram.WebApp.HapticFeedback.impactOccurred('heavy');
                setTimeout(() => {
                    window.location.href = this.getAttribute('href');
                }, 300);
            });
        });
    </script>
    """
    from web.templates.base import get_base_template
    return get_base_template("Physical Wellness", content, "physical_health")