import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="A list of 7290 unique names that would appear in a cyberpunk novel. Each name is unisex, and hints at a racially and ethnically diverse genderqueer future, with some names more traditional and others inside jokes or crew nicknames.\n\n1. Ace\n2. Acid\n3. Aja\n4. Akira\n5. Alpha\n6. Angel\n7. Arclight\n8. Ash\n9. Azrael\n10. Banshee\n11. Beijing\n12. Beta\n13. Blackout\n14. Blaze\n15. Boomer\n16. Boston\n17. Breaker\n18. Bullet\n19. Butter\n20. Buzz\n21. Cairo\n22. Chrome\n23. Circuit\n24. Crow\n25. Dallas\n26. Delta\n27. Detroit\n28. Diablo\n29. Dice\n30. Digital\n31. Domino\n32. Echo\n33. Ember\n34. Fang\n35. Fargo\n36. Fenix\n37. Fever\n38. Five\n39. Flash\n40. Ghost\n41. Golem\n42. Havoc\n43. Helsinki\n44. Hex\n45. Highway\n46. Hunter\n47. India\n48. Infected\n49. Interface\n50. Istanbul\n51. Jackal\n52. Jakarta\n53. Jericho\n54. Jet\n55. Jolt\n56. Judge\n57. Juno\n58. Kabuki\n59. Kai\n60. Key\n61. Killer\n62. King\n63. Knight\n64. Lacuna\n65. Laser\n66. Leech\n67. Legion\n68. Leopard\n69. Lima\n70. Lock\n71. London\n72. Lynch\n73. Malta\n74. Manila\n75. Marlowe\n76. Matrix\n77. Max\n78. Mayhem\n79. Mechanic\n80. Medina\n81. Memphis\n82. Mercer\n83. Mexico\n84. Mirage\n85. Monaco\n86. Montreal\n87. Mosaic\n88. Moscow\n89. Neon\n90. Nighthawk\n91. Ninja\n92. Nomad\n93. Nyx\n94. Oblivion\n95. Oracle\n96. Oslo\n97. Outlaw\n98. Oz\n99. Phoenix\n100. Pilot\n101. Piranha\n102. Plague\n103. Poker\n104. Psycho\n105. Punk\n106. Pyramid\n107. Queen\n108. Rabbit\n109. Racer\n110. Radar\n111. Rager\n112. Raider\n113. Ranger\n114. Rapier\n115. Reaper\n116. Rebel\n117. Red\n118. Rome\n119. Rook\n120. Router\n121. Runner\n122. Rush\n123. Sabre\n124. Sage\n125. Samurai\n126. Scar\n127. Shadow\n128. Shanghai\n129. Siren\n130. Sniper\n131. Soldier\n132. Solo\n133. Spectre\n134. Sphinx\n135. Spyder\n136. Stallion\n137.Star\n138. Stinger\n139. Stranger\n140. Swede\n141. Switch\n142. Sydney\n143. Tank\n144. Tokyo\n145. Tracker\n146. Trinity\n147. Vegas\n148. Venice\n149. Viper\n150. Warlock\n151. Whiskey\n152. Wichita\n153. Widow\n154. Wolf\n155. Wraith\n156. Zero",
  temperature=.8,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)