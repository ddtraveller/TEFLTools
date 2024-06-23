class Spells:
    def __init__(self):
        self.movement_spells = [
            {"name": "Swift Wind's Blessing", "description": "Increases the caster's movement speed.", "effect": {"stat": "movement_speed", "value": 2, "duration": "1 hour"}},
            {"name": "Bounding Stride", "description": "Allows the caster to make long jumps.", "effect": {"stat": "jump_distance", "value": 10, "duration": "instant"}},
            {"name": "Soaring Flight", "description": "Grants the caster the ability to fly.", "effect": {"stat": "flight_speed", "value": 60, "duration": "10 minutes"}},
            {"name": "Nimble Retreat", "description": "Allows the caster to quickly escape from combat.", "effect": {"stat": "movement_speed", "value": 4, "duration": "1 minute"}},
            {"name": "Dimensional Passage", "description": "Teleports the caster a short distance.", "effect": {"stat": "teleport_distance", "value": 30, "duration": "instant"}},
            {"name": "Galloping Speed", "description": "Increases the caster's movement speed while mounted.", "effect": {"stat": "mounted_speed", "value": 3, "duration": "1 hour"}},
            {"name": "Ascending Motion", "description": "Allows the caster to walk on vertical surfaces.", "effect": {"stat": "wall_walking", "value": True, "duration": "10 minutes"}},
            {"name": "Brisk Pace", "description": "Increases the caster's walking speed.", "effect": {"stat": "walking_speed", "value": 1, "duration": "1 hour"}}
        ]
        self.sorcery_spells = [
            {"name": "Mighty Bolt", "description": "Fires a powerful bolt of energy at the target.", "effect": {"stat": "damage", "value": "3d6", "duration": "instant"}},
            {"name": "Furious Blast", "description": "Unleashes a blast of destructive energy.", "effect": {"stat": "damage", "value": "4d8", "duration": "instant"}},
            {"name": "Wrathful Curse", "description": "Curses the target, reducing their combat effectiveness.", "effect": {"stat": "attack_bonus", "value": -2, "duration": "1 minute"}},
            {"name": "Scorching Ray", "description": "Shoots a ray of intense heat at the target.", "effect": {"stat": "damage", "value": "2d8", "duration": "instant"}},
            {"name": "Devouring Plague", "description": "Inflicts a debilitating plague on the target.", "effect": {"stat": "constitution", "value": -4, "duration": "1 hour"}},
            {"name": "Heavenly Fireball", "description": "Conjures a massive fireball that explodes on impact.", "effect": {"stat": "damage", "value": "6d6", "duration": "instant"}},
            {"name": "Forceful Arrows", "description": "Enhances the caster's arrows with magical force.", "effect": {"stat": "arrow_damage", "value": "1d6", "duration": "1 minute"}},
            {"name": "Hexing Chant", "description": "Chants a hex that weakens the target's defenses.", "effect": {"stat": "armor_class", "value": -2, "duration": "1 minute"}}
        ]
        self.elemental_spells = [
            {"name": "Burning Touch", "description": "Sets the target on fire with a touch.", "effect": {"stat": "fire_damage", "value": "1d6", "duration": "instant"}},
            {"name": "Tempestuous Gust", "description": "Creates a powerful gust of wind to push enemies back.", "effect": {"stat": "push_distance", "value": 10, "duration": "instant"}},
            {"name": "Thunderous Clap", "description": "Claps hands together, creating a thunderous shockwave.", "effect": {"stat": "thunder_damage", "value": "2d6", "duration": "instant"}},
            {"name": "Stony Grasp", "description": "Causes stone to grasp and restrain the target.", "effect": {"stat": "restrained", "value": True, "duration": "1 minute"}},
            {"name": "Elemental Attunement", "description": "Attunes the caster to a chosen element, granting resistance.", "effect": {"stat": "elemental_resistance", "value": 5, "duration": "1 hour"}},
            {"name": "Freezing Breath", "description": "Exhales a breath of frigid air, freezing the target.", "effect": {"stat": "cold_damage", "value": "2d8", "duration": "instant"}},
            {"name": "Tremoring Earth", "description": "Causes the ground to tremble and shake.", "effect": {"stat": "difficult_terrain", "value": True, "duration": "1 minute"}},
            {"name": "Entangling Vines", "description": "Summons vines to entangle and restrain the target.", "effect": {"stat": "restrained", "value": True, "duration": "1 minute"}}
        ]
        self.healing_spells = [
            {"name": "Purifying Light", "description": "Bathes the target in purifying light, removing negative effects.", "effect": {"stat": "remove_negative_effects", "value": True, "duration": "instant"}},
            {"name": "Blessed Regeneration", "description": "Accelerates the target's natural healing process.", "effect": {"stat": "hit_point_regeneration", "value": 2, "duration": "1 minute"}},
            {"name": "Divine Guidance", "description": "Grants the target divine guidance, increasing their wisdom.", "effect": {"stat": "wisdom", "value": 2, "duration": "1 hour"}},
            {"name": "Lifeforce Infusion", "description": "Infuses the target with vital lifeforce, restoring hit points.", "effect": {"stat": "hit_points", "value": "3d8", "duration": "instant"}},
            {"name": "Cleansing Ritual", "description": "Performs a ritual to cleanse the target of curses and diseases.", "effect": {"stat": "remove_curses_diseases", "value": True, "duration": "instant"}},
            {"name": "Circle of Protection", "description": "Creates a protective circle around the target, granting temporary hit points.", "effect": {"stat": "temporary_hit_points", "value": 10, "duration": "1 minute"}},
            {"name": "Calming Influence", "description": "Exerts a calming influence on the target, reducing their stress and anxiety.", "effect": {"stat": "stress_reduction", "value": 5, "duration": "1 hour"}},
            {"name": "Sacred Darshan", "description": "Grants the target a sacred vision, increasing their insight.", "effect": {"stat": "insight", "value": 2, "duration": "1 hour"}},
            {"name": "Heightened Senses", "description": "Heightens the target's senses, increasing their perception.", "effect": {"stat": "perception", "value": 2, "duration": "1 hour"}},
            {"name": "Protect the Fallen", "description": "Creates a protective barrier around a fallen ally, shielding them from further harm.", "effect": {"stat": "damage_reduction", "value": 5, "duration": "1 minute"}}
        ]
        self.nature_spells = [
            {"name": "Bountiful Growth", "description": "Accelerates the growth of plants in the area.", "effect": {"stat": "plant_growth", "value": 2, "duration": "24 hours"}},
            {"name": "Primal Summoning", "description": "Summons a beast or plant creature to aid the caster.", "effect": {"stat": "summon_creature", "value": True, "duration": "1 hour"}},
            {"name": "Verdant Barrier", "description": "Creates a wall of dense foliage, blocking movement.", "effect": {"stat": "movement_blocked", "value": True, "duration": "10 minutes"}},
            {"name": "Graceful Camouflage", "description": "Camouflages the caster, blending them into the natural surroundings.", "effect": {"stat": "stealth", "value": 5, "duration": "1 hour"}},
            {"name": "Herbal Remedy", "description": "Creates a healing salve from natural herbs.", "effect": {"stat": "hit_points", "value": "2d6", "duration": "instant"}},
            {"name": "Thorny Entanglement", "description": "Causes thorny vines to sprout and entangle the target.", "effect": {"stat": "restrained", "value": True, "duration": "1 minute"}},
            {"name": "Swarming Insects", "description": "Summons a swarm of insects to harass and distract enemies.", "effect": {"stat": "distraction", "value": True, "duration": "1 minute"}},
            {"name": "Awakening Touch", "description": "Awakens the natural spirits within plants and animals.", "effect": {"stat": "awaken_nature", "value": True, "duration": "1 hour"}}
        ]
        self.internal_spells = [
            {"name": "Unbreakable Armor", "description": "Surrounds the caster with an unbreakable armor of energy.", "effect": {"stat": "armor_class", "value": 4, "duration": "1 minute"}},
            {"name": "Radiant Aura", "description": "Emanates a radiant aura that protects and inspires allies.", "effect": {"stat": "morale_bonus", "value": 2, "duration": "1 minute"}},
            {"name": "Insightful Vision", "description": "Grants the caster a moment of profound insight and clarity.", "effect": {"stat": "critical_chance", "value": 5, "duration": "1 minute"}},
            {"name": "Unyielding Fortitude", "description": "Fills the caster with unyielding fortitude, increasing their endurance.", "effect": {"stat": "constitution", "value": 2, "duration": "1 hour"}},
            {"name": "Inner Cultivation", "description": "Allows the caster to cultivate their inner strength and potential.", "effect": {"stat": "strength", "value": 2, "duration": "1 hour"}},
            {"name": "Resolute Stance", "description": "Grants the caster a resolute stance, increasing their stability and balance.", "effect": {"stat": "saving_throw_bonus", "value": 2, "duration": "1 minute"}},
            {"name": "Prescient Foresight", "description": "Grants the caster a brief glimpse into the immediate future.", "effect": {"stat": "initiative", "value": 5, "duration": "1 minute"}},
            {"name": "Invulnerable Mind", "description": "Fortifies the caster's mind against mental attacks and manipulation.", "effect": {"stat": "wisdom_saving_throw", "value": 5, "duration": "1 hour"}}
        ]
        self.mystic_spells = [
            {"name": "Third Eye Revelation", "description": "Opens the caster's third eye, revealing hidden truths.", "effect": {"stat": "detect_illusion", "value": True, "duration": "1 minute"}},
            {"name": "Oracular Divination", "description": "Allows the caster to divine the future through mystical means.", "effect": {"stat": "divination", "value": True, "duration": "instant"}},
            {"name": "Nature's Wisdom", "description": "Grants the caster wisdom and understanding from the natural world.", "effect": {"stat": "nature_knowledge", "value": 5, "duration": "1 hour"}},
            {"name": "Scholarly Insight", "description": "Provides the caster with scholarly insight into a specific topic.", "effect": {"stat": "knowledge", "value": 5, "duration": "1 hour"}},
            {"name": "Predictive Calculation", "description": "Enables the caster to make precise predictions and calculations.", "effect": {"stat": "intelligence", "value": 2, "duration": "1 hour"}},
            {"name": "Spiritual Sight", "description": "Allows the caster to perceive spiritual entities and energies.", "effect": {"stat": "detect_spirits", "value": True, "duration": "1 minute"}},
            {"name": "Ancestral Knowledge", "description": "Grants the caster access to the knowledge and wisdom of their ancestors.", "effect": {"stat": "history_knowledge", "value": 5, "duration": "1 hour"}},
            {"name": "Intuitive Perception", "description": "Enhances the caster's intuition and perception of their surroundings.", "effect": {"stat": "perception", "value": 2, "duration": "1 hour"}}
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