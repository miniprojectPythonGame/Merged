character_1 = {
    'name': 'MorganaF',
    'spec': 'Warrior',
    'level': 25,
    'img': '../images/characters/warrior_1_rect.jpg'
}

character_2 = {
    'name': 'AdrianPL',
    'spec': 'Mage',
    'level': 67,
    'img': '../images/characters/mage_1_rect.jpg',
    'img_full': "../images/characters/mage_1.jpg",
    "health": 120,
    "gold": 1250,
    "eq": {
        "helmet": None,
        "chestplate": None,
        "gloves": None,
        "boots": None,
        "necklace": None,
        "belt": {
            "name": 'Leather Belt',
            "img_path": '../images/items/armor/belt.png',
            "type": 'common',
        },
        "ring": None,
        "artefact": None,
    },
    "backpacks": [
        [
            {
                "name": 'Cool club',
                "img_path": '../images/items/weapons/club.png',
                "type": 'legendary',
            },
            {
                "name": 'Pretty ok hammer',
                "img_path": '../images/items/weapons/hammer.png',
                "type": 'epic',
            },
            {
                "name": 'Meh dagger',
                "img_path": '../images/items/weapons/dagger.png',
                "type": 'common',
            },
            {
                "name": 'I guess it is an ax',
                "img_path": '../images/items/weapons/ax.png',
                "type": 'common',
            },
            {
                "name": 'Just health potion',
                "img_path": '../images/items/magic/potion.png',
                "type": 'common',
            },
            {
                "name": 'Dragonscale Belt',
                "img_path": '../images/items/armor/belt.png',
                "type": 'legendary',
            },
        ],
        [
            {
                "name": 'Ok club',
                "img_path": '../images/items/weapons/club.png',
                "type": 'common',
            },
        ]
    ],
    "statistics": {
        "strength": 11,
        "intelligence": 170,
        "dexterity": 56,
        "constitution": 4,
        "luck": 21,
        "protection": 40,
        "persuasion": 64,
        "trade": 39,
        "leadership": 100,
        "initiative": 86,
    }
}

armor_shop = {
    "headgear": [
        {
            "name": 'headgear #1',
            "img_path": '../images/items/armor/headgear.png',
            "type": 'legendary',
        },
        {
            "name": 'headgear #2',
            "img_path": '../images/items/armor/headgear.png',
            "type": 'common',
        },
        {
            "name": 'headgear #3',
            "img_path": '../images/items/armor/headgear.png',
            "type": 'epic',
        },
        {
            "name": 'headgear #4',
            "img_path": '../images/items/armor/headgear.png',
            "type": 'common',
        },
    ],
    "breastplate": [
        {
            "name": 'breastplate #1',
            "img_path": '../images/items/armor/breastplate.png',
            "type": 'common',
        },
        {
            "name": 'breastplate #2',
            "img_path": '../images/items/armor/breastplate.png',
            "type": 'common',
        },
        {
            "name": 'breastplate #3',
            "img_path": '../images/items/armor/breastplate.png',
            "type": 'epic',
        },
        {
            "name": 'breastplate #4',
            "img_path": '../images/items/armor/breastplate.png',
            "type": 'legendary',
        },
    ],
    "gloves": [
        {
            "name": 'Gloves #1',
            "img_path": '../images/items/armor/gloves.png',
            "type": 'common',
        },
        {
            "name": 'Gloves #2',
            "img_path": '../images/items/armor/gloves.png',
            "type": 'legendary',
        },
        {
            "name": 'Gloves #3',
            "img_path": '../images/items/armor/gloves.png',
            "type": 'epic',
        },
    ],
    "boots": [
        {
            "name": 'Boots #1',
            "img_path": '../images/items/armor/boots.png',
            "type": 'common',
        },
        {
            "name": 'Boots #2',
            "img_path": '../images/items/armor/boots.png',
            "type": 'common',
        },
        {
            "name": 'Boots #3',
            "img_path": '../images/items/armor/boots.png',
            "type": 'legendary',
        },
        {
            "name": 'Boots #4',
            "img_path": '../images/items/armor/boots.png',
            "type": 'common',
        },
    ],
    "belts": [
        {
            "name": 'Belt #1',
            "img_path": '../images/items/armor/belt.png',
            "type": 'legendary',
        },
        {
            "name": 'Belt #2',
            "img_path": '../images/items/armor/belt.png',
            "type": 'epic',
        },
    ]
}

weapon_shop = {
    "swords": [
        {
            "name": 'Sword #1',
            "img_path": '../images/items/weapons/sword.png',
            "type": 'legendary',
        },
        {
            "name": 'Sword #2',
            "img_path": '../images/items/weapons/sword.png',
            "type": 'common',
        },
        {
            "name": 'Sword #3',
            "img_path": '../images/items/weapons/sword.png',
            "type": 'epic',
        },
        {
            "name": 'Sword #4',
            "img_path": '../images/items/weapons/sword.png',
            "type": 'common',
        },
    ],
    "shields": [
        {
            "name": 'Shield #1',
            "img_path": '../images/items/weapons/shield.png',
            "type": 'common',
        },
        {
            "name": 'Shield #2',
            "img_path": '../images/items/weapons/shield.png',
            "type": 'common',
        },
        {
            "name": 'Shield #3',
            "img_path": '../images/items/weapons/shield.png',
            "type": 'epic',
        },
        {
            "name": 'Shield #4',
            "img_path": '../images/items/weapons/shield.png',
            "type": 'legendary',
        },
    ],
    "hammers": [
        {
            "name": 'Hammer #1',
            "img_path": '../images/items/weapons/hammer.png',
            "type": 'common',
        },
        {
            "name": 'Hammer #2',
            "img_path": '../images/items/weapons/hammer.png',
            "type": 'legendary',
        },
        {
            "name": 'Hammer #3',
            "img_path": '../images/items/weapons/hammer.png',
            "type": 'epic',
        },
    ],
    "bows": [
        {
            "name": 'Bow #1',
            "img_path": '../images/items/weapons/bow.png',
            "type": 'common',
        },
        {
            "name": 'Bow #2',
            "img_path": '../images/items/weapons/bow.png',
            "type": 'common',
        },
        {
            "name": 'Bow #3',
            "img_path": '../images/items/weapons/bow.png',
            "type": 'legendary',
        },
        {
            "name": 'Bow #4',
            "img_path": '../images/items/weapons/bow.png',
            "type": 'common',
        },
    ],
    "daggers": [
        {
            "name": 'Dagger #1',
            "img_path": '../images/items/weapons/dagger.png',
            "type": 'legendary',
        },
        {
            "name": 'Dagger #2',
            "img_path": '../images/items/weapons/dagger.png',
            "type": 'epic',
        },
    ]
}

magic_shop = {
    "potions": [
        {
            "name": 'Health Potion #1',
            "img_path": '../images/items/magic/potion.png',
            "type": 'legendary',
        },
        {
            "name": 'Strength Potion #2',
            "img_path": '../images/items/magic/potion.png',
            "type": 'common',
        },
        {
            "name": 'Speed Potion #3',
            "img_path": '../images/items/magic/potion.png',
            "type": 'epic',
        },
    ],
    "rings": [
        {
            "name": 'Ring #1',
            "img_path": '../images/items/magic/ring.png',
            "type": 'common',
        },
        {
            "name": 'Ring #2',
            "img_path": '../images/items/magic/ring.png',
            "type": 'legendary',
        },
        {
            "name": 'Ring #3',
            "img_path": '../images/items/magic/ring.png',
            "type": 'epic',
        },
    ],
    "necklaces": [
        {
            "name": 'Necklace #1',
            "img_path": '../images/items/magic/necklace.png',
            "type": 'common',
        },
        {
            "name": 'Necklace #2',
            "img_path": '../images/items/magic/necklace.png',
            "type": 'common',
        },
        {
            "name": 'Necklace #3',
            "img_path": '../images/items/magic/necklace.png',
            "type": 'legendary',
        },
        {
            "name": 'Necklace #4',
            "img_path": '../images/items/magic/necklace.png',
            "type": 'common',
        },
    ],
    "sceptres": [
        {
            "name": 'Sceptre #1',
            "img_path": '../images/items/magic/sceptre.png',
            "type": 'legendary',
        },
        {
            "name": 'Sceptre #2',
            "img_path": '../images/items/magic/sceptre.png',
            "type": 'epic',
        },
    ]
}

tavern_quests = [
    # QUEST #1
    {
        "name": 'Zlecenie na dziką kobrę',
        "difficulty": 'easy',
        "min_level": 12,
        "min_gold_reward": 510,
        "max_gold_reward": 720,
        "description": ["Lorem ipsum dolor sit amet, consectetur",
                        "adipiscing elit. Vivamus vel ultrices eros.",
                        "Vestibulum eu odio commodo, dignissim dolor",
                        "vel, venenatis velit. Vivamus non odio a",
                        "ante posuere blandit. Nam tincidunt augue",
                        "faucibus quam lobortis, lacinia maximus",
                        "sapien auctor. Aliquam vel velit diam."],
        "treasure": [
            {
                "name": 'Sceptre #1',
                "img_path": '../images/items/magic/sceptre.png',
                "type": 'legendary',
            },
            {
                "name": 'Strength Potion #2',
                "img_path": '../images/items/magic/potion.png',
                "type": 'common',
            },
            {
                "name": 'Gloves #2',
                "img_path": '../images/items/armor/gloves.png',
                "type": 'legendary',
            },
        ]
    },
    # QUEST #2
    {
        "name": 'Rzężenie pod podłogą',
        "difficulty": 'intermediate',
        "min_level": 25,
        "min_gold_reward": 1050,
        "max_gold_reward": 1300,
        "description": ["Lorem ipsum dolor sit amet, consectetur",
                        "adipiscing elit. Vivamus vel ultrices eros.",
                        "Vestibulum eu odio commodo, dignissim dolor",
                        "vel, venenatis velit. Vivamus non odio a",
                        "ante posuere blandit. Nam tincidunt augue",
                        "faucibus quam lobortis, lacinia maximus",
                        "sapien auctor. Aliquam vel velit diam."],
        "treasure": [
            {
                "name": 'Ring #2',
                "img_path": '../images/items/magic/ring.png',
                "type": 'legendary',
            },
            {
                "name": 'Sword #3',
                "img_path": '../images/items/weapons/sword.png',
                "type": 'epic',
            },
        ]
    },
    # QUEST #3
    {
        "name": 'Zagubiony indeks',
        "difficulty": 'hard',
        "min_level": 33,
        "min_gold_reward": 1080,
        "max_gold_reward": 1920,
        "description": ["Lorem ipsum dolor sit amet, consectetur",
                        "adipiscing elit. Vivamus vel ultrices eros.",
                        "Vestibulum eu odio commodo, dignissim dolor",
                        "vel, venenatis velit. Vivamus non odio a",
                        "ante posuere blandit. Nam tincidunt augue",
                        "faucibus quam lobortis, lacinia maximus",
                        "sapien auctor. Aliquam vel velit diam."],
        "treasure": [
            {
                "name": 'Boots #3',
                "img_path": '../images/items/armor/boots.png',
                "type": 'legendary',
            },
            {
                "name": 'Chestplate #3',
                "img_path": '../images/items/armor/chestplate.png',
                "type": 'epic',
            },
            {
                "name": 'Sword #3',
                "img_path": '../images/items/weapons/sword.png',
                "type": 'epic',
            },
        ]
    },
    # QUEST #4
    {
        "name": 'Nawiedzona katedra',
        "difficulty": 'easy',
        "min_level": 10,
        "min_gold_reward": 334,
        "max_gold_reward": 675,
        "description": ["Lorem ipsum dolor sit amet, consectetur",
                        "adipiscing elit. Vivamus vel ultrices eros.",
                        "Vestibulum eu odio commodo, dignissim dolor",
                        "vel, venenatis velit. Vivamus non odio a",
                        "ante posuere blandit. Nam tincidunt augue",
                        "faucibus quam lobortis, lacinia maximus",
                        "sapien auctor. Aliquam vel velit diam."],
        "treasure": [
            {
                "name": 'Helmet #4',
                "img_path": '../images/items/armor/helmet.png',
                "type": 'common',
            },
            {
                "name": 'Belt #2',
                "img_path": '../images/items/armor/belt.png',
                "type": 'epic',
            },
        ]
    },
]