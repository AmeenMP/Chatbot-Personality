from enum import Enum

openness_options = ["creative", "imaginative", "curious", "open-minded", "adventurous"]
conscientiousness_options = ["organized", "disciplined", "responsible", "dependable", "meticulous"]
extraversion_options = ["outgoing", "energetic", "sociable", "talkative", "enthusiastic"]
agreeableness_options = ["friendly", "compassionate", "cooperative", "empathetic", "kind"]
neuroticism_options = ["anxious", "moody", "sensitive", "nervous", "emotional"]


class TraitName(Enum):
    OPENNESS = "Openness"
    CONSCIENTIOUSNESS = "Conscientiousness"
    EXTRAVERSION = "Extraversion"
    AGREEABLENESS = "Agreeableness"
    NEUROTICISM = "Neuroticism"
