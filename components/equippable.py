from __future__ import annotations

from typing import TYPE_CHECKING

import sys
sys.path.append('../tcod_tutorial_v2')
from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
	from entity import Item


class Equippable(BaseComponent):
	parent: Item

	def __init__(
		self,
		equipment_type: EquipmentType,
		power_bonus: int = 0,
		defense_bonus: int = 0,
		attack_bonus: int = 0,
		armor_bonus: int = 0,
		recipe = ["unobtanium"],
		craft_level = 5
	):
		self.equipment_type = equipment_type

		self.power_bonus = power_bonus
		self.attack_bonus = attack_bonus
		self.armor_bonus = armor_bonus
		self.defense_bonus = defense_bonus
		self.craft_level = craft_level

		self.recipe = recipe

class pair_of_2_by_arm_guards(Equippable):
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 5,
					craft_level = 1,
					recipe = [['2x4', 1], ['rag', 1]])

class pair_of_chitin_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['string_36', 1], ['string_6', 4], ['chitin_piece', 4], ['leather', 4]])

class pair_of_hard_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['neoprene', 6], ['plastic_chunk', 8]])

class pair_of_leather_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 6,
					craft_level = 3,
					recipe = [['leather', 12], ['fur', 12]])

class pair_of_steel_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['steel_lump', 6], ['steel_chunk', 24], ['fur', 6], ['leather', 6]])

class pair_of_metal_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 4,
					armor_bonus = 6,
					craft_level = 4,
					recipe = [['sheet_metal_small', 4]])

class pair_of_scrap_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['scrap', 60]])

class pair_of_neoprene_arm_sleeves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 3,
					recipe = [['neoprene', 4], ['rag', 2]])

class pair_of_chainmail_sleeves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['link_sheet', 3], ['chain_link', 75], ['wire', 1], ['fur', 6], ['leather', 6]])

class pair_of_elbow_pads(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 4,
					craft_level = 4,
					recipe = [['plastic_chunk', 4], ['rag', 2], ['leather', 2], ['fur', 2]])

class pair_of_leather_vambraces(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 4,
					craft_level = 2,
					recipe = [['leather', 4], ['fur', 4]])

class pair_of_cord_sandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 4,
					craft_level = 2,
					recipe = [['filament', 140, 'LIST']])

class pair_of_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 2,
					recipe = [['leather', 10]])

class pair_of_chitinous_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['chitin_piece', 16], ['leather', 16]])

class pair_of_biosilicified_chitin_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 5,
					recipe = [['acidchitin_piece', 16], ['leather', 16]])

class pair_of_survivor_fireboots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 8,
					recipe = [['nomex', 8], ['kevlar_plate', 4], ['duct_tape', 200], ['nomex_socks', 1], ['boots_combat', 1], ['boots_steel', 1], ['boots_bunker', 1]])

class pair_of_fur_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 2,
					recipe = [['leather', 7], ['fur', 7]])

class pair_of_survivor_wetsuit_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['plastic_chunk', 4], ['kevlar_plate', 4], ['duct_tape', 200], ['wetsuit_booties', 1], ['boots_combat', 1], ['boots_steel', 1], ['boots_bunker', 1]])

class pair_of_heavy_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 7,
					armor_bonus = 7,
					craft_level = 7,
					recipe = [['rag', 4], ['leather', 4], ['steel_chunk', 4], ['scrap', 12], ['kevlar_plate', 4], ['duct_tape', 100], ['boots_combat', 1], ['boots_steel', 1], ['boots_hiking', 1], ['boots_bunker', 1], ['boots', 1]])

class pair_of_leather_armor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 6,
					craft_level = 2,
					recipe = [['leather', 18], ['fur', 18]])

class pair_of_light_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['rag', 8], ['kevlar_plate', 4], ['duct_tape', 100], ['boots_combat', 1], ['boots_steel', 1], ['boots_hiking', 1], ['boots_bunker', 1], ['boots', 1]])

class pair_of_armored_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['fur', 16], ['leather', 16]])

class pair_of_scrap_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['scrap', 50]])

class pair_of_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['leather', 8], ['kevlar_plate', 4], ['duct_tape', 100], ['boots_combat', 1], ['boots_steel', 1], ['boots_hiking', 1], ['boots_bunker', 1], ['boots', 1]])

class pair_of_winter_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['felt_patch', 20], ['bag_plastic', 8]])

class pair_of_winter_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['fur', 12], ['kevlar_plate', 4], ['duct_tape', 100], ['boots_combat', 1], ['boots_steel', 1], ['boots_hiking', 1], ['boots_bunker', 1], ['boots', 1]])

class pair_of_XL_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['leather', 24], ['rag', 6], ['scrap', 4], ['boots_combat', 2], ['kevlar_plate', 10], ['duct_tape', 200]])

class pair_of_wooden_clogs(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 4,
					armor_bonus = 6,
					craft_level = 3,
					recipe = [['2x4', 2], ['stick', 2]])

class pair_of_geta(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 1,
					recipe = [['2x4', 1], ['cordage_short', 1, 'LIST']])

class pair_of_leather_sandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 3,
					craft_level = 1,
					recipe = [['leather', 3]])

class pair_of_moccasins(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 4,
					craft_level = 1,
					recipe = [['fur', 2]])

class pair_of_birchbark_shoes(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 4,
					craft_level = 2,
					recipe = [['birchbark', 3]])

class pair_of_straw_sandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 3,
					craft_level = 1,
					recipe = [['straw_pile', 4], ['birchbark', 6]])

class pair_of_swim_fins(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['plastic_chunk', 8], ['duct_tape', 80], ['medical_tape', 80], ['superglue', 1]])

class pair_of_swimming_booties(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['neoprene', 2], ['rag', 2]])

class pair_of_chainmail_chausses(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['link_sheet', 2], ['chain_link', 50], ['wire', 1], ['rag', 4]])

class pair_of_flame_resistant_socks(Equippable):
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['nomex', 9]])

class pair_of_wool_socks(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 5,
					craft_level = 1,
					recipe = [['yarn', 75]])

class pair_of_stockings(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 1,
					recipe = [['rag', 8]])

class pair_of_tabi(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 5,
					craft_level = 1,
					recipe = [['rag', 3]])

class pair_of_chainmail_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['link_sheet', 2], ['chain_link', 50], ['wire', 1], ['rag', 4]])

class pair_of_chitinous_gauntlets(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['cordage_superior', 1, 'LIST'], ['chitin_piece', 3], ['leather', 3]])

class pair_of_biosilicified_chitin_gauntlets(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 5,
					recipe = [['cordage_superior', 1, 'LIST'], ['acidchitin_piece', 3], ['leather', 3]])

class pair_of_leather_armor_gauntlets(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 5,
					craft_level = 2,
					recipe = [['leather', 6], ['fur', 6]])

class pair_of_armored_fingerless_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 1,
					recipe = [['gloves_fingerless', 1], ['scrap', 2]])

class pair_of_survivor_firegloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 8,
					recipe = [['nomex', 6], ['leather', 2], ['duct_tape', 120], ['gloves_tactical', 1], ['kevlar_plate', 4], ['nomex_gloves', 1], ['fire_gauntlets', 1]])

class pair_of_fur_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 2,
					recipe = [['fur', 4]])

class pair_of_heavy_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 4,
					armor_bonus = 6,
					craft_level = 7,
					recipe = [['rag', 2], ['leather', 2], ['scrap', 4], ['duct_tape', 50], ['gloves_tactical', 1], ['kevlar_plate', 4], ['gloves_leather', 1], ['gloves_light', 1], ['gloves_liner', 1], ['wetsuit_gloves', 1], ['fire_gauntlets', 1]])

class pair_of_leather_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 2,
					recipe = [['leather', 2]])

class pair_of_light_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 1,
					recipe = [['rag', 4]])

class pair_of_glove_liners(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 1,
					recipe = [['rag', 2]])

class pair_of_light_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['rag', 6], ['leather', 2], ['duct_tape', 80], ['gloves_tactical', 1], ['kevlar_plate', 4], ['gloves_leather', 1], ['gloves_light', 1], ['gloves_liner', 1], ['wetsuit_gloves', 1], ['fire_gauntlets', 1]])

class pair_of_armored_gauntlets(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['fur', 10], ['leather', 10]])

class pair_of_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['rag', 2], ['leather', 6], ['duct_tape', 80], ['gloves_tactical', 1], ['kevlar_plate', 4], ['gloves_leather', 1], ['gloves_light', 1], ['gloves_liner', 1], ['wetsuit_gloves', 1], ['fire_gauntlets', 1]])

class pair_of_wool_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 1,
					recipe = [['felt_patch', 4]])

class pair_of_work_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 2,
					recipe = [['leather', 2], ['gloves_leather', 1], ['rag', 2], ['gloves_light', 1]])

class pair_of_winter_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['rag', 2], ['fur', 8], ['duct_tape', 80], ['gloves_tactical', 1], ['kevlar_plate', 4], ['gloves_leather', 1], ['gloves_light', 1], ['gloves_liner', 1], ['wetsuit_gloves', 1], ['fire_gauntlets', 1]])

class pair_of_XL_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['leather', 16], ['rag', 6], ['scrap', 2], ['duct_tape', 160], ['gloves_tactical', 2], ['kevlar_plate', 6]])

class pair_of_mittens(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 1,
					recipe = [['yarn', 250]])

class pair_of_flame_resistant_gloves(Equippable):
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['nomex', 6]])

class barbute_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['fur', 4], ['leather', 4]])

class chitinous_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['cordage_superior', 1, 'LIST'], ['chitin_piece', 6], ['leather', 6]])

class conical_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['fur', 6]])

class biosilicified_chitin_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 5,
					recipe = [['cordage_superior', 1, 'LIST'], ['acidchitin_piece', 6], ['leather', 6]])

class galea(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['fur', 4], ['leather', 4]])

class kabuto(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 9,
					recipe = [['fur', 14], ['leather', 14], ['rag', 4]])

class leather_armor_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['leather', 16], ['fur', 16]])

class nasal_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['fur', 3], ['leather', 3]])

class nomad_cowl(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['hat_ball', 1], ['hat_boonie', 1], ['glasses_safety', 1], ['glasses_bal', 1], ['leather', 8]])

class great_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['fur', 4], ['leather', 4]])

class scavenger_cowl(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 8,
					recipe = [['hat_ball', 1], ['hat_boonie', 1], ['mask_filter', 1], ['glasses_bal', 1], ['goggles_ski', 1], ['kevlar_plate', 8]])

class scrap_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['scrap', 30]])

class survivor_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['helmet_liner', 1], ['hat_cotton', 1], ['rag', 3], ['tac_helmet', 1], ['tac_fullhelmet', 1], ['helmet_army', 1], ['kevlar_plate', 6], ['hood_rain', 1], ['bag_plastic', 2], ['leather', 8], ['duct_tape', 150], ['helmet_riot', 1], ['helmet_motor', 1], ['helmet_football', 1], ['helmet_ball', 1], ['helmet_skid', 1], ['helmet_bike', 1], ['hat_hard', 1], ['firehelmet', 1], ['pickelhaube', 1], ['plastic_chunk', 8]])

class XL_survivor_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['scrap', 4], ['rag', 6], ['leather', 16], ['plastic_chunk', 20], ['kevlar_plate', 14], ['hood_rain', 2], ['bag_plastic', 4], ['duct_tape', 300]])

class heavy_survivor_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 7,
					armor_bonus = 7,
					craft_level = 7,
					recipe = [['helmet_liner', 1], ['hat_cotton', 1], ['rag', 3], ['helmet_army', 1], ['hood_rain', 1], ['bag_plastic', 2], ['steel_chunk', 2], ['scrap', 6], ['duct_tape', 75], ['helmet_riot', 1], ['helmet_motor', 1], ['helmet_football', 1], ['helmet_ball', 1], ['helmet_skid', 1], ['helmet_bike', 1], ['hat_hard', 1], ['firehelmet', 1], ['pickelhaube', 1], ['plastic_chunk', 8]])

class Corinthian_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 5,
					armor_bonus = 6,
					craft_level = 6,
					recipe = [['scrap_bronze', 7], ['fur', 4], ['leather', 4]])

class pair_of_2_by_shin_guards(Equippable):
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 5,
					craft_level = 1,
					recipe = [['2x4', 1], ['rag', 4]])

class chainmail_leggings(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['link_sheet', 4], ['chain_link', 100], ['wire', 1], ['rag', 6]])

class leather_chaps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['leather', 8]])

class pair_of_knee_pads(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 4,
					craft_level = 4,
					recipe = [['plastic_chunk', 8], ['rag', 4], ['leather', 4], ['fur', 4]])

class pair_of_bronze_greaves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['fur', 6], ['leather', 6], ['scrap_bronze', 12]])

class pair_of_hard_leg_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['neoprene', 6], ['plastic_chunk', 8]])

class pair_of_steel_leg_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['fur', 6], ['leather', 6]])

class pair_of_iron_greaves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['fur', 6], ['leather', 6]])

class pair_of_scrap_leg_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['scrap', 60]])

class light_survivor_cargo_pants(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['rag', 15], ['bag_plastic', 4], ['legrig', 1], ['tool_belt', 1], ['ragpouch', 4], ['leather_pouch', 2], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 50], ['kevlar_plate', 8]])

class survivor_cargo_pants(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['pants_army', 1], ['pants_cargo', 1], ['shorts_cargo', 1], ['kevlar', 1], ['modularvest', 1], ['kevlar_plate', 12], ['rag', 12], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 4], ['leather_pouch', 2], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 100]])

class AEP_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 6,
					craft_level = 6,
					recipe = [['cleansuit', 1], ['duct_tape', 600], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24], ['plastic_sheet', 1]])

class ANBC_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 6,
					craft_level = 8,
					recipe = [['hazmat_suit', 1], ['duct_tape', 800], ['swat_armor', 1], ['kevlar_plate', 48], ['plastic_sheet', 1]])

class boiled_leather_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 4,
					armor_bonus = 6,
					craft_level = 3,
					recipe = [['water', 10], ['water_clean', 10], ['wax', 2], ['any_tallow', 8, 'LIST'], ['vinegar', 10], ['pine_bough', 20], ['salt', 50], ['armor_larmor', 1], ['armguard_larmor', 1]])

class chitinous_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['chitin_piece', 36], ['leather', 36]])

class biosilicified_chitin_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 0,
					armor_bonus = 4,
					craft_level = 5,
					recipe = [['acidchitin_piece', 36], ['leather', 36]])

class fur_body_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 6,
					craft_level = 5,
					recipe = [['fur', 48]])

class leather_body_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 6,
					craft_level = 5,
					recipe = [['leather', 30], ['fur', 30]])

class plate_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 8,
					recipe = [['fur', 20], ['leather', 20]])

class nomad_gear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['duster', 1], ['vest', 1], ['tacvest', 1], ['ragpouch', 1], ['leather_pouch', 1], ['dump_pouch', 1], ['fanny', 1], ['tool_belt', 1], ['legrig', 1], ['pants_cargo', 1], ['pants_army', 1], ['leather', 24]])

class light_nomad_gear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['tunic', 1], ['shorts_cargo', 1], ['shorts_denim', 1], ['vest', 1], ['tacvest', 1], ['ragpouch', 2], ['dump_pouch', 2], ['fanny', 2], ['tool_belt', 1], ['legrig', 1], ['rag', 20]])

class plated_leather_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 3,
					armor_bonus = 6,
					craft_level = 2,
					recipe = [['steel_chunk', 6], ['scrap', 18], ['armor_larmor', 1], ['armguard_larmor', 1]])

class ornamental_plate_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 9,
					recipe = [['fur', 16], ['leather', 16]])

class O_yoroi(Equippable):
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 9,
					recipe = [['fur', 28], ['leather', 28], ['rag', 10]])

class scavenger_gear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 8,
					recipe = [['jacket_army', 1], ['vest', 1], ['tacvest', 1], ['mbag', 1], ['runner_bag', 1], ['fanny', 2], ['dump_pouch', 1], ['tool_belt', 1], ['legrig', 1], ['pants_army', 1], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class scrap_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['scrap', 170]])

class chainmail_hauberk(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 2,
					recipe = [['chainmail_vest', 1], ['chainmail_arms', 1], ['chainmail_legs', 1], ['gambeson', 1]])

class chainmail_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['chainmail_hood', 1], ['chainmail_vest', 1], ['chainmail_arms', 1], ['chainmail_legs', 1], ['gambeson', 1]])

class faraday_chainmail_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['link_sheet', 2], ['chainmail_hood', 1], ['link_sheet', 7], ['chainmail_vest', 1], ['link_sheet', 3], ['chainmail_arms', 1], ['link_sheet', 4], ['chainmail_legs', 1], ['link_sheet', 2], ['chainmail_hands', 1], ['link_sheet', 2], ['chainmail_feet', 1], ['chain_link', 500], ['wire', 5], ['rag', 26]])

class entry_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['nomex', 40], ['kevlar_plate', 8], ['duct_tape', 200], ['superglue', 5], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class survivor_firesuit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 8,
					recipe = [['rag', 4], ['nomex_suit', 1], ['entry_suit', 1], ['nomex', 20], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 200], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class gambeson(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 4,
					recipe = [['rag', 26]])

class heavy_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['rag', 20], ['leather', 20], ['steel_chunk', 4], ['scrap', 12], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 300], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class light_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['rag', 30], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 200], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class flame_resistant_suit(Equippable):
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['nomex', 18]])

class survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['rag', 20], ['leather', 20], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 300], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class winter_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['rag', 10], ['leather', 20], ['fur', 20], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 300], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class XL_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 6,
					recipe = [['rag', 30], ['leather', 40], ['scrap', 8], ['coat_rain', 2], ['jacket_windbreaker', 2], ['jacket_evac', 2], ['coat_gut', 2], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 400], ['kevlar', 2], ['modularvest', 2], ['swat_armor', 2], ['kevlar_plate', 42]])

class XL_heavy_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 8,
					recipe = [['rag', 30], ['leather', 40], ['steel_chunk', 8], ['scrap', 24], ['coat_rain', 2], ['jacket_windbreaker', 2], ['jacket_evac', 2], ['coat_gut', 2], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 400], ['kevlar', 2], ['modularvest', 2], ['swat_armor', 2], ['kevlar_plate', 48]])

class bell_cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 5,
					armor_bonus = 6,
					craft_level = 5,
					recipe = [['scrap_bronze', 28]])

class lamellar_cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['cordage_superior', 4, 'LIST'], ['rag', 4], ['leather', 42], ['fur', 42]])

class lorica_segmentata(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['fur', 12], ['leather', 12]])

class bookplate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 4,
					armor_bonus = 6,
					craft_level = 3,
					recipe = [['paper', 1200], ['duct_tape', 150]])

class chainmail_vest(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 7,
					recipe = [['link_sheet', 7], ['chain_link', 175], ['wire', 1], ['rag', 6]])

class cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 8,
					recipe = [['fur', 6], ['leather', 6]])

class scrap_cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['scrap', 80]])

class armored_leather_jacket(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['jacket_leather', 1], ['jacket_leather_red', 1], ['scrap', 9]])

class light_survivor_body_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 1,
					armor_bonus = 5,
					craft_level = 5,
					recipe = [['rag', 15], ['coat_rain', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 2], ['leather_pouch', 2], ['dump_pouch', 1], ['purse', 1], ['fanny', 1], ['duct_tape', 150], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 16]])

class armored_leather_vest(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, 
					defense_bonus = 2,
					armor_bonus = 5,
					craft_level = 3,
					recipe = [['vest_leather', 1], ['scrap', 5]])

