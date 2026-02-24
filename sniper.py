cat << 'EOF' > index.html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sniper Immobilier | Prestige & Sécurité en Algérie</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root { --dark-bg: #0f172a; --gold: #d4af37; }
        body { background-color: var(--dark-bg); color: white; font-family: 'Inter', sans-serif; margin: 0; overflow-x: hidden; }
        .bg-flag {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('https://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Algeria.svg');
            background-size: cover; background-position: center; opacity: 0.04; z-index: -1; pointer-events: none;
        }
        h1, h2 { font-family: 'Playfair Display', serif; }
        .gold-border { border: 1px solid rgba(212, 175, 55, 0.3); }
        .gold-text { color: var(--gold); }
    </style>
</head>
<body>
    <div class="bg-flag"></div>
    <nav class="max-w-7xl mx-auto p-6 flex justify-between items-center">
        <img src="logo.png" alt="Sniper Immobilier" class="h-14">
        <a href="https://wa.me/33634089609" class="bg-white/5 border border-white/10 px-5 py-2 rounded-full hover:bg-white/10 transition text-sm font-medium">
            Contact Direct
        </a>
    </nav>
    <header class="max-w-5xl mx-auto py-24 px-6 text-center">
        <h1 class="text-5xl md:text-7xl mb-6 leading-tight">Bâtissez votre <span class="gold-text italic">Patrimoine</span> en Algérie</h1>
        <p class="text-gray-400 text-xl font-light max-w-2xl mx-auto leading-relaxed">
            Une sélection rigoureuse de propriétés d'exception, accompagnée d'une expertise juridique sans compromis.
        </p>
    </header>
    <section class="max-w-7xl mx-auto px-6 py-12">
        <h2 class="text-3xl mb-12 italic text-center md:text-left">Sélections Prioritaires</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div class="bg-white/5 rounded-2xl overflow-hidden gold-border hover:bg-white/10 transition">
                <div class="h-64 bg-gray-800 flex items-center justify-center italic text-gray-600 font-light">Visuel en attente</div>
                <div class="p-8">
                    <span class="text-xs font-semibold tracking-widest uppercase text-yellow-600">Alger | Hydra</span>
                    <h3 class="text-xl font-bold mt-2 mb-3 italic text-white">Résidence des Ambassadeurs</h3>
                    <p class="text-gray-400 text-sm leading-relaxed mb-6 font-light">Vérification foncière effectuée par nos experts. Dossier juridique complet et sécurisé.</p>
                    <div class="flex justify-between items-center border-t border-white/10 pt-6">
                        <span class="text-lg font-semibold">Prix sur demande</span>
                        <a href="https://wa.me/33634089609" class="text-sm gold-text hover:underline font-bold uppercase tracking-tighter">S'informer</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <footer class="mt-24 py-12 border-t border-white/5 text-center text-gray-500 text-xs tracking-widest uppercase">
        &copy; 2026 Sniper Immobilier Algérie — Prestige & Rigueur
    </footer>
</body>
</html>
EOF