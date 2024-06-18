class Spells:
    def __init__(self):
        self.movement_spells = [
            "Swift Wind's Blessing", "Bounding Stride", "Soaring Flight", "Nimble Retreat",
            "Dimensional Passage", "Galloping Speed", "Ascending Motion", "Brisk Pace"
        ]
        self.sorcery_spells = [
            "Mighty Bolt", "Furious Blast", "Wrathful Curse", "Scorching Ray",
            "Devouring Plague", "Heavenly Fireball", "Forceful Arrows", "Hexing Chant"
        ]
        self.elemental_spells = [
            "Burning Touch", "Tempestuous Gust", "Thunderous Clap", "Stony Grasp",
            "Elemental Attunement", "Freezing Breath", "Tremoring Earth", "Entangling Vines"
        ]
        self.healing_spells = [
            "Purifying Light", "Blessed Regeneration", "Divine Guidance", "Lifeforce Infusion",
            "Cleansing Ritual", "Circle of Protection", "Calming Influence", "Sacred Darshan",
            "Heightened Senses", "Protect the Fallen"
        ]
        self.nature_spells = [
            "Bountiful Growth", "Primal Summoning", "Verdant Barrier", "Graceful Camouflage",
            "Herbal Remedy", "Thorny Entanglement", "Swarming Insects", "Awakening Touch"
        ]
        self.internal_spells = [
            "Unbreakable Armor", "Radiant Aura", "Insightful Vision", "Unyielding Fortitude",
            "Inner Cultivation", "Resolute Stance", "Prescient Foresight", "Invulnerable Mind"
        ]
        self.mystic_spells = [
            "Third Eye Revelation", "Oracular Divination", "Nature's Wisdom", "Scholarly Insight",
            "Predictive Calculation", "Spiritual Sight", "Ancestral Knowledge", "Intuitive Perception"
        ]

        self.spell_types = {
            "Movement": ["Rogue", "Wizard"],
            "Sorcery": ["Wizard"],
            "Elemental": ["Wizard"],
            "Healing": ["Cleric", "Paladin", "Shaman", "Monk"],
            "Nature": ["Ranger", "Shaman", "Barbarian"],
            "Internal": ["Monk", "Martial Artist"],
            "Mystic": ["Shaman", "Monk"]
        }