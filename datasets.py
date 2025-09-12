#here we will have data sets only
training_data = [
    # SPAGHETTI - 8 different ways to ask
    "How to make spaghetti",
    """For spaghetti:
Ingredients:
- 400g (1 lb) dried spaghetti
- 2 tbsp olive oil
- 3 cloves garlic, thinly sliced
- 400g (14 oz) canned crushed tomatoes or marinara sauce
- 1 tsp dried oregano, salt and pepper to taste
- 2 tbsp butter (optional)
- Fresh basil leaves and grated Parmesan to serve

Steps:
1. Bring a large pot of water to a rolling boil. Add a generous pinch of salt (it should taste like sea water).
2. Add the spaghetti and cook uncovered, stirring occasionally, for 8–10 minutes until al dente (check package times).
3. While pasta cooks, heat olive oil in a skillet over medium heat. Add garlic and sauté 30–60 seconds until fragrant — do not burn.
4. Add crushed tomatoes, oregano, salt, and pepper. Simmer 8–12 minutes until slightly reduced. Stir in butter at the end for richness if desired.
5. Drain pasta, reserving ½ cup pasta water. Toss pasta with sauce, adding reserved water a little at a time to coat and bind the sauce.
6. Serve hot with torn basil and a generous sprinkle of grated Parmesan.

Tips:
- Use starchy pasta water to help the sauce cling to the noodles.
- For a meat version, brown 250–300g ground beef or sausage and add it to the sauce.
- Store leftovers in an airtight container for 3–4 days; reheat with a splash of water or olive oil.""",

    "How do I make spaghetti",
    """For spaghetti:
Ingredients:
- 400g spaghetti
- 2 tbsp olive oil
- 2 tbsp unsalted butter (optional)
- 3 cloves garlic, chopped
- 1 can (400g) crushed tomatoes
- 1 tsp sugar (if tomatoes are acidic)
- Salt, pepper, fresh basil, grated Parmesan

Procedure:
1. Boil salted water and cook spaghetti until al dente.
2. In a saucepan, heat oil and butter, saute garlic briefly, add crushed tomatoes, sugar, salt, pepper. Simmer 10 minutes.
3. Toss drained spaghetti with sauce, add reserved pasta water to loosen if needed.
4. Plate and finish with basil and Parmesan.

Notes:
- Add chili flakes for heat or sauté onions before garlic for more depth.
- Fresh tomatoes (peeled and chopped) may be used when in season.""",

    "Recipe for spaghetti",
    """For spaghetti:
Ingredients and steps as above — boil pasta salted, make a simple garlic-tomato sauce, toss together, finish with herbs and cheese. (See longer recipe above for proportions and tips.)""",

    "Can you give me spaghetti recipe",
    """For spaghetti:
Follow the detailed garlic-tomato recipe: boil pasta, simmer sauce with garlic and canned tomatoes, mix with pasta and finish with basil and Parmesan. Use starchy pasta water to emulsify the sauce.""",

    "How to cook spaghetti",
    """For spaghetti:
Bring salted water to a boil, cook spaghetti 8–10 minutes to al dente, make sauce by sautéing garlic in olive oil then adding tomatoes and simmering, combine pasta and sauce, garnish with basil and cheese.""",

    "Make spaghetti",
    """For spaghetti:
Prepare by cooking pasta in salted boiling water and making a simple tomato-garlic sauce. Toss and serve hot with cheese. See full recipe above for exact quantities and tips.""",

    "Show me how to make spaghetti",
    """For spaghetti:
Boil salted water, cook spaghetti until al dente. Sauté garlic in olive oil, add crushed tomatoes and seasonings, simmer, then toss pasta with sauce using reserved pasta water to bind. Top with basil and Parmesan.""",

    "Best way to make spaghetti",
    """For spaghetti:
Use good-quality dried pasta, heavily salted boiling water, and finish the sauce by tossing hot pasta in the pan so the flavors marry. Use reserved pasta water and a knob of butter to create a glossy sauce; add fresh herbs and grated Parmesan before serving.""",


    # PANCAKES - 8 different ways to ask
    "How to make pancakes",
    """For fluffy pancakes:
Ingredients:
- 1½ cups (190g) all-purpose flour
- 3½ tsp baking powder
- 1 tbsp sugar
- ¼ tsp salt
- 1¼ cups (300 ml) milk
- 1 large egg
- 3 tbsp melted butter or vegetable oil
- 1 tsp vanilla extract (optional)

Steps:
1. In a bowl, whisk flour, baking powder, sugar, and salt.
2. In another bowl, whisk milk, egg, melted butter, and vanilla.
3. Pour wet into dry and stir until just combined — batter should be slightly lumpy; do not overmix.
4. Preheat a non-stick pan or griddle over medium heat. Lightly grease.
5. Pour ¼ cup batter per pancake. Cook until bubbles form and edges look set (2–3 min), flip and cook 1–2 minutes more until golden.
6. Serve warm with butter, syrup, jam, or fruit.

Tips:
- For extra fluffy pancakes, let batter rest 5–10 minutes.
- Add mashed banana, blueberries, or chocolate chips to the batter when pouring.""",

    "How do I make pancakes",
    """For fluffy pancakes:
Combine dry ingredients (flour, baking powder, sugar, salt). Combine wet (milk, egg, melted butter). Mix until just combined, cook on medium heat, flip when bubbly, serve warm with toppings.""",

    "Recipe for pancakes",
    """For fluffy pancakes:
See complete ingredient list and steps above — key points: don't overmix the batter and cook on medium heat so the center cooks without burning the outside.""",

    "Can you give me pancake recipe",
    """For fluffy pancakes:
Use 1½ cups flour, 3½ tsp baking powder, 1¼ cups milk, 1 egg, and 3 tbsp melted butter. Mix wet and dry separately, combine gently, cook on a greased griddle until golden. Top as desired.""",

    "How to cook pancakes",
    """For fluffy pancakes:
Preheat pan, pour batter in ¼ cup portions, wait for bubbles, flip and finish. Keep cooked pancakes warm in low oven while finishing the batch.""",

    "Make pancakes",
    """For fluffy pancakes:
Follow the same steps: mix dry and wet ingredients separately, combine, then cook pancakes on a medium-hot griddle until golden. Add fruits or spices to vary flavor.""",

    "Show me how to make pancakes",
    """For fluffy pancakes:
Whisk dry ingredients; whisk milk, egg, and melted butter; fold together; cook on a buttered pan until bubbles appear then flip; serve hot with toppings.""",

    "Best pancake recipe",
    """For fluffy pancakes:
Use fresh baking powder (for lift), separate and whip the egg white for extra fluff if you want, and rest the batter briefly. Serve immediately for best texture.""",


    # CHICKEN CURRY - 8 different ways to ask
    "How to make chicken curry",
    """For a simple chicken curry (serves 4):
Ingredients:
- 800g (1.7 lb) chicken pieces (bone-in or boneless)
- 2 medium onions, finely chopped
- 3 cloves garlic, minced
- 1-inch ginger, grated
- 2 tomatoes, chopped (or 1 cup canned tomato puree)
- 2 tsp ground coriander, 1 tsp cumin, 1 tsp turmeric
- 1–2 tsp chili powder (adjust)
- 1 tsp garam masala (optional)
- 3 tbsp oil
- Salt, fresh cilantro for garnish
- 200 ml water or as needed

Steps:
1. Heat oil in a heavy pot. Add chopped onions and cook until golden brown (this builds flavor).
2. Add garlic and ginger; sauté 1–2 minutes.
3. Add spices (coriander, cumin, turmeric, chili) and toast briefly until aromatic.
4. Add tomatoes and cook until oil separates and tomatoes soften (8–10 minutes). If using puree, simmer 5–7 minutes.
5. Add chicken pieces, stir to coat with masala. Sear for 3–4 minutes.
6. Add water to cover partially, bring to gentle simmer, cover and cook 20–30 minutes (longer for bone-in) until chicken is cooked through and tender.
7. Sprinkle garam masala, adjust salt, simmer 2 more minutes. Garnish with cilantro.
8. Serve with steamed rice, roti, or naan.

Tips:
- For creamier curry, add 2–3 tbsp yogurt or coconut milk at the end.
- Browned onions and properly cooked tomatoes are key to a rich gravy.
- Leftovers taste even better the next day; refrigerate 3–4 days or freeze.""",

    "How do I make chicken curry",
    """For a simple chicken curry:
Sauté onions until golden, add garlic/ginger, add spices and tomatoes, add chicken, simmer until tender. Finish with garam masala and cilantro. Serve with rice or bread.""",

    "Recipe for chicken curry",
    """For a simple chicken curry:
Ingredients: chicken, onions, garlic, ginger, tomatoes, coriander, cumin, turmeric, chili powder, oil, salt. Cook onions until brown, add spices, tomatoes, chicken, and simmer until done. Add yogurt or cream to finish if desired.""",

    "Can you give me chicken curry recipe",
    """For a simple chicken curry:
Follow the steps above; key is to brown the onions well and simmer the chicken until tender. Adjust chili and spices to your taste. Garnish with fresh cilantro before serving.""",

    "How to cook chicken curry",
    """For a simple chicken curry:
Start with a hot pan, brown onions, add spice mix and tomatoes, then the chicken. Simmer covered until cooked and tender; adjust seasoning and add cream or yogurt if you want a richer sauce.""",

    "Make chicken curry",
    """For a simple chicken curry:
Make a masala base with onions, garlic, ginger and spices, add chicken and simmer in the gravy until tender. Serve hot with rice or flatbreads.""",

    "Show me how to make chicken curry",
    """For a simple chicken curry:
Sauté onions; add ginger/garlic; add ground spices; add tomatoes and cook until the oil separates; add chicken and water; simmer until done; finish with garam masala and cilantro.""",

    "Best way to make chicken curry",
    """For a simple chicken curry:
Brown onions slowly for deep flavor, toast spices before adding tomatoes, use bone-in chicken for more flavor, and simmer slowly for tender meat. Finish with a splash of cream or yogurt for silkiness.""",


    # FRIED RICE - 8 different ways to ask
    "How to make fried rice",
    """For simple egg fried rice (serves 3-4):
Ingredients:
- 3 cups cooked and chilled rice (day-old is best)
- 2 eggs, beaten
- 1 cup mixed vegetables (peas, carrots, corn)
- 2–3 spring onions, chopped
- 2–3 tbsp soy sauce
- 1 tbsp sesame oil or vegetable oil
- 1–2 tbsp neutral oil for frying
- Salt and pepper to taste

Steps:
1. Heat a wok or large skillet over high heat. Add neutral oil.
2. Add beaten eggs, scramble quickly, then remove and set aside.
3. Add a little more oil, stir-fry vegetables until just tender.
4. Add chilled rice, break clumps, and stir-fry until rice is hot. Add soy sauce and sesame oil, tossing to coat evenly.
5. Return scrambled eggs to the pan, stir in spring onions, season, and serve immediately.

Tips:
- Use day-old rice to avoid mushy texture.
- Add cooked chicken, shrimp, or tofu for protein.
- High heat and quick tossing give the best texture and slight char.""",

    "How do I make fried rice",
    """For simple egg fried rice:
Use chilled rice, high heat, scramble eggs separately, stir-fry vegetables, add rice and soy sauce, toss with sesame oil and green onions at the end.""",

    "Recipe for fried rice",
    """For simple egg fried rice:
Cook rice ahead and chill. Stir-fry eggs and veggies, then add rice and soy sauce. Toss quickly on high heat and finish with sesame oil and scallions.""",

    "Can you give me fried rice recipe",
    """For simple egg fried rice:
Use leftover rice, high heat, soy sauce to taste, and add proteins or vegetables as desired. Serve piping hot.""",

    "How to cook fried rice",
    """For simple egg fried rice:
Preheat wok, add oil, scramble eggs, fry veggies, add rice and sauces, toss until hot and slightly toasted, garnish with scallions.""",

    "Make fried rice",
    """For simple egg fried rice:
Follow the cooked-chilled-rice approach: separate egg scrambling, high-heat stir-fry, soy + sesame finish. Add proteins or chili for variation.""",

    "Show me how to make fried rice",
    """For simple egg fried rice:
Scramble eggs, set aside. Stir-fry veggies, add rice and sauces, return eggs, toss and serve. High heat and chilled rice make it great.""",

    "Best fried rice recipe",
    """For simple egg fried rice:
Use day-old rice, prepped mise-en-place, and high heat. Toast rice lightly for texture, use light soy plus a touch of sesame oil, and finish with fresh scallions or cilantro.""",


    # CHOCOLATE CAKE - 8 different ways to ask
    "How to make chocolate cake",
    """For a basic moist chocolate cake (one 9-inch round):
Ingredients:
- 1¾ cups (220g) all-purpose flour
- 1¾ tsp baking powder
- 1¾ tsp baking soda
- ¾ cup (75g) cocoa powder
- 1½ cups (300g) sugar
- 2 large eggs
- 1 cup (240 ml) milk
- ½ cup (120 ml) vegetable oil
- 2 tsp vanilla extract
- 1 cup (240 ml) boiling water
- Pinch of salt

Steps:
1. Preheat oven to 350°F (175°C). Grease and flour a 9-inch pan.
2. In a bowl, sift flour, cocoa, baking powder, baking soda, and salt. In another bowl, whisk sugar, eggs, milk, oil, and vanilla.
3. Combine wet and dry ingredients until smooth. Stir in boiling water slowly — batter will be thin.
4. Pour into the pan and bake 30–35 minutes or until a toothpick comes out clean.
5. Cool completely before frosting. Use chocolate buttercream, ganache, or dust with powdered sugar.

Tips:
- Use good quality cocoa for flavor. The hot water blooms the cocoa and gives a moist texture.
- For extra moisture, replace some milk with sour cream or yogurt.""",

    "How do I make chocolate cake",
    """For a basic moist chocolate cake:
Mix dry ingredients; mix wet ingredients; combine; add boiling water; bake 30–35 minutes at 350°F/175°C. Cool and frost.""",

    "Recipe for chocolate cake",
    """For a basic moist chocolate cake:
See above ingredient list and method — important steps: sift cocoa and dry ingredients, add boiling water, and avoid overbaking for moist crumb.""",

    "Can you give me chocolate cake recipe",
    """For a basic moist chocolate cake:
Use 1¾ cups flour, ¾ cup cocoa, 1½ cups sugar, 2 eggs, 1 cup milk, ½ cup oil, and 1 cup boiling water. Mix and bake as directed. Frost once cool.""",

    "How to cook chocolate cake",
    """For a basic moist chocolate cake:
Preheat oven, combine dry/wet, add boiling water to loosen batter, bake until a skewer is clean, then cool and frost.""",

    "Make chocolate cake",
    """For a basic moist chocolate cake:
Follow the list above. Use either buttercream or chocolate ganache to finish. Let the cake cool completely before frosting to avoid melting the frosting.""",

    "Show me how to make chocolate cake",
    """For a basic moist chocolate cake:
Sift and combine dry ingredients, whisk wet ingredients, mix, add boiling water, bake at 350°F (175°C) for 30–35 minutes, cool, and frost.""",

    "Best chocolate cake recipe",
    """For a basic moist chocolate cake:
Use high-quality cocoa, add boiling water to bloom the cocoa, and consider using sour cream for extra tenderness. Do a toothpick test to avoid overbaking.""",


    # MOMO (Nepali/Tibetan dumplings) - 8 different ways to ask
    "How to make momo",
    """For Nepali/Tibetan momos (makes ~30):
Dough:
- 3 cups all-purpose flour
- ~1 cup water
- Pinch of salt

Filling (chicken):
- 400g minced chicken
- 1 medium onion, finely chopped
- 3 cloves garlic, minced
- 1-inch ginger, minced
- 2 tbsp soy sauce
- 1 tsp salt, pepper, 1 tsp sesame oil (optional)
- Finely chopped cilantro (optional)

Steps:
1. Make dough: mix flour and salt, add water gradually, knead until smooth. Rest 20–30 minutes covered.
2. Make filling: mix minced chicken with onion, garlic, ginger, soy sauce, salt, pepper and oil. Keep filling cold.
3. Divide dough into golf-ball pieces, roll into thin circles (3–4 inch). Place 1–2 tsp filling in center. Fold and pleat edges to seal (many styles).
4. Steam: Arrange momos in a steamer lined with cabbage or parchment. Steam 12–15 minutes until filling is cooked (adjust for size).
5. Serve hot with a spicy tomato-ginger dipping sauce or achar.

Tips:
- For juicier momos add a small amount of fat (chicken skin or a spoon of oil) or finely chopped vegetables.
- You can pan-fry the steamed momos after steaming to make “kothey” style crispy bottoms.
- Leftover filling can be frozen; also freeze assembled momos on a tray and then bag them for longer storage.""",

    "How do I make momo",
    """For Nepali/Tibetan momos:
Make a simple flour dough, prepare a savory filling (chicken, pork, or veg), shape dumplings, and steam ~12–15 minutes. Serve with achar or spicy sauce.""",

    "Recipe for momo",
    """For Nepali/Tibetan momos:
Dough: flour + water + pinch salt. Filling: minced meat or veggies with onion, garlic, ginger, soy sauce. Fill wrappers, pleat, steam, and serve with dipping sauce.""",

    "Can you give me momo recipe",
    """For Nepali/Tibetan momos:
Detailed recipe above — key: roll thin wrappers, don't overfill, and steam until cooked. Adjust spice and herbs to taste.""",

    "How to cook momo",
    """For Nepali/Tibetan momos:
Assemble filled dumplings and steam 12–15 minutes, or steam then pan-fry for a crispy bottom. Serve immediately with achar.""",

    "Make momo",
    """For Nepali/Tibetan momos:
Prepare dough and filling, form momos by pleating, steam until cooked through. Try vegetable filling or classic chicken/pork.""",

    "Show me how to make momo",
    """For Nepali/Tibetan momos:
Knead dough, prepare filling seasoning well, roll wrappers thin, place filling, pleat and seal, steam 12–15 minutes. Serve hot with spicy tomato-ginger chutney.""",

    "Best momo recipe",
    """For Nepali/Tibetan momos:
Use fresh minced meat, finely chop aromatics (onion, garlic, ginger), keep filling moist but not watery, and steam on medium heat until fully cooked. Serve with homemade achar for the best flavor.""",
]


training_data_more = [
    # DAL (Simple Nepali/Indian style) - 8 phrasings
    "How to make dal",
    """For simple yellow dal (serves 4):
Ingredients:
- 1 cup yellow split pigeon peas (toor dal) or red lentils (masoor dal)
- 3 cups water (more for preferred consistency)
- 1 medium tomato, chopped
- 1 small onion, finely chopped (optional)
- 2 cloves garlic, minced
- 1/2 inch ginger, minced
- 1/2 tsp turmeric powder
- 1 tsp cumin seeds
- 2 tbsp oil or ghee
- Salt to taste
- Fresh cilantro for garnish
Tadka (tempering):
- 1 tbsp ghee or oil
- 1/2 tsp mustard seeds (optional)
- 1/2 tsp cumin seeds
- 1 dried red chili or 1/2 tsp chili flakes
Steps:
1. Rinse the dal until water runs clear. In a pot or pressure cooker, combine dal, water, turmeric, and a pinch of salt. Cook until soft (20–30 min simmer or 1–2 whistles in a pressure cooker).
2. In a separate pan, heat oil/ghee, sauté onions (if using) until translucent, add garlic and ginger, cook 1 minute.
3. Add chopped tomato and simmer until soft. Add this cooked masala to the cooked dal and simmer 5–10 minutes; adjust consistency with water.
4. For tadka: heat ghee/oil in a small pan, add mustard seeds (if using) and cumin, then dried chili. When fragrant, pour over the dal.
5. Garnish with chopped cilantro and serve hot with steamed rice or roti.

Tips:
- Mash a few spoonfuls of dal to make it creamier.
- Adjust spice levels; a squeeze of lemon brightens the dal.""",

    "How do I make dal",
    """For simple yellow dal:
Cook lentils until soft, prepare a tomato-onion-ginger-garlic base, combine, add a hot tadka of spices at the end, garnish with cilantro, and serve with rice or bread.""",

    "Recipe for dal",
    """For simple yellow dal:
See full recipe above — key points: rinse lentils well, cook until very soft, and finish with a hot tempering (tadka) for aroma.""",

    "Can you give me dal recipe",
    """For simple yellow dal:
Use 1 cup lentils to 3 cups water, turmeric, and salt. Cook until soft, add a simple tomato-garlic masala, finish with spiced tadka and cilantro.""",

    "How to cook dal",
    """For simple yellow dal:
Boil lentils until tender, simmer them with sautéed onion-tomato-ginger-garlic, and add tadka of cumin/mustard seeds in hot oil for fragrance.""",

    "Make dal",
    """For simple yellow dal:
Prepare lentils and a light masala, combine, and finish with a hot spiced oil (tadka). Serve with rice or flatbread.""",

    "Show me how to make dal",
    """For simple yellow dal:
Rinse and boil lentils; make a quick onion-tomato-garlic base; mix, simmer to combine flavors; top with tempered spices in hot oil and garnish with cilantro.""",

    "Best dal recipe",
    """For simple yellow dal:
Slow-cook the dal for creaminess, caramelize onions for deeper flavor, use fresh spices, and always finish with a tadka for the best aroma and taste.""",


    # BUTTER CHICKEN - 8 phrasings
    "How to make butter chicken",
    """For butter chicken (Murgh Makhani) — serves 4:
Ingredients:
- 700–800g chicken (boneless thighs preferred), cut into bite-sized pieces
Marinade:
- 1/2 cup yogurt
- 1 tsp ginger paste, 1 tsp garlic paste
- 1 tsp turmeric, 1 tsp garam masala, 1 tsp chili powder, salt
Gravy:
- 3 tbsp butter + 1 tbsp oil
- 1 large onion, finely chopped
- 3 cloves garlic, 1-inch ginger, minced
- 2 cups tomato puree (canned or fresh)
- 1 tsp ground cumin, 1 tsp coriander powder
- 1/2 cup heavy cream (or cashew paste for richness)
- 1 tsp sugar (optional), salt to taste
- 1 tsp kasuri methi (dried fenugreek leaves), crushed
Steps:
1. Marinate chicken in yogurt and spices at least 30 minutes (overnight better).
2. Sear or grill marinated chicken pieces until lightly charred and mostly cooked; set aside.
3. In a pan, heat butter+oil. Sauté onions until golden. Add garlic and ginger; cook briefly.
4. Add tomato puree and spices; simmer 10–12 minutes until oil separates and sauce thickens.
5. Add cream, return chicken to pan, simmer 8–12 minutes until chicken cooked through and sauce coats the pieces.
6. Finish with crushed kasuri methi and a knob of butter for gloss. Serve with naan or basmati rice.

Tips:
- Use boneless dark meat (thighs) for moist chicken.
- Grilling or broiling the marinated chicken adds smoky flavor.
- Substitute cream with blended cashews for a dairy-free/ richer texture.""",

    "How do I make butter chicken",
    """For butter chicken:
Marinate chicken in spiced yogurt, sear, make a tomato-onion gravy, add cream, simmer with chicken until tender, finish with fenugreek and butter; serve with rice or bread.""",

    "Recipe for butter chicken",
    """For butter chicken:
See above: key steps are marination, charring the chicken, and simmering in a creamy tomato-based gravy with kasuri methi for that characteristic flavor.""",

    "Can you give me butter chicken recipe",
    """For butter chicken:
Marinate chicken in yogurt and spices, sear, prepare a rich tomato-cream gravy, combine and simmer, finish with butter and dried fenugreek leaves.""",

    "How to cook butter chicken",
    """For butter chicken:
Sear marinated chicken; make a tomato and cream gravy; add chicken; simmer on low until tender; finish with butter and kasuri methi for aroma.""",

    "Make butter chicken",
    """For butter chicken:
Follow the marinade-grill-simmer method: yogurt-marinated chicken + creamy tomato gravy + kasuri methi + butter = classic butter chicken.""",

    "Show me how to make butter chicken",
    """For butter chicken:
Marinate, brown the chicken, build the tomato gravy by cooking out rawness, add cream and chicken, finish with fenugreek and butter; serve hot.""",

    "Best butter chicken recipe",
    """For butter chicken:
Marinate overnight, use grilled chicken for smoky notes, and balance tomato acidity with a touch of sugar or milk; finish with butter and crushed kasuri methi for authentic depth.""",


    # HOMEMADE PIZZA (Basic) - 8 phrasings
    "How to make pizza at home",
    """For a basic homemade pizza (makes 2 medium pizzas):
Dough:
- 3½ cups (420g) all-purpose flour
- 1 tsp sugar, 2 tsp salt
- 2 tsp instant yeast
- 1¼ cups warm water (about 110°F/43°C)
- 2 tbsp olive oil
Sauce & Toppings:
- 1 cup tomato sauce or pizza sauce
- 1–2 cups shredded mozzarella
- Toppings of choice (pepperoni, mushrooms, bell peppers, onions, olives, basil)
Steps:
1. Mix flour, salt, and yeast. Add warm water and olive oil; knead until smooth (8–10 min). Let rise in an oiled bowl covered until doubled (1–1.5 hours).
2. Preheat oven to highest setting (250–260°C / 475–500°F). If you have a pizza stone, heat it in the oven.
3. Divide dough into two, shape into rounds, stretch or roll thin to desired thickness.
4. Spread a thin layer of pizza sauce, sprinkle cheese, and add toppings (don’t overload).
5. Bake 10–12 minutes until crust is golden and cheese bubbly. Remove and finish with fresh basil and drizzle of olive oil.

Tips:
- For crisp crust, bake hot and fast; use a pizza stone if available.
- Let dough rise slowly in the fridge overnight for better flavor.""",

    "How do I make pizza at home",
    """For a basic homemade pizza:
Make a simple yeast dough, let rise, top with sauce and cheese, bake in a very hot oven until crust is golden and cheese melts.""",

    "Recipe for homemade pizza",
    """For a basic homemade pizza:
See dough and sauce above — key points: high oven temperature and not overloading toppings.""",

    "Can you give me pizza recipe",
    """For a basic homemade pizza:
Use a well-kneaded dough risen until doubled, use a simple tomato sauce, top sparingly and bake hot for a crisp crust and well-melted cheese.""",

    "How to cook pizza at home",
    """For a basic homemade pizza:
Preheat oven very hot, stretch dough thin, add sauce, cheese, and toppings, bake 10–12 minutes or until done.""",

    "Make homemade pizza",
    """For a basic homemade pizza:
Follow steps for dough, sauce, and baking. Finish with fresh herbs and a drizzle of olive oil for more flavor.""",

    "Show me how to make pizza at home",
    """For a basic homemade pizza:
Knead and proof dough, spread sauce, add cheese and toppings, bake in hot oven or on pizza stone, and serve hot.""",

    "Best homemade pizza recipe",
    """For a basic homemade pizza:
Use a hot oven, allow a slow cold fermentation for the dough if possible, use high-quality mozzarella, and finish with fresh basil and a sprinkle of good olive oil.""",


    # CAESAR SALAD - 8 phrasings
    "How to make Caesar salad",
    """For a classic Caesar salad (serves 2–3):
Ingredients:
- 1 large head romaine lettuce, washed and torn
- 1/2 cup croutons (homemade or store-bought)
Dressing:
- 1 egg yolk (or 1 tbsp mayonnaise for safety)
- 1 tsp Dijon mustard
- 1–2 anchovy fillets, mashed (or 1/2 tsp anchovy paste; optional)
- 1 garlic clove, minced
- 2 tbsp lemon juice
- 1/3 cup olive oil
- 2 tbsp grated Parmesan
- Salt and pepper to taste
Steps:
1. In a bowl, whisk egg yolk with mustard, garlic, mashed anchovy, and lemon juice. Slowly stream in olive oil while whisking to emulsify. Stir in Parmesan, salt and pepper.
2. Toss romaine with enough dressing to coat, add croutons and extra Parmesan on top.
3. Optionally top with grilled chicken or shrimp for a main course.

Notes:
- If you’re uncomfortable using raw egg, use pasteurized yolk or mayonnaise as a substitute.
- Anchovy adds the classic umami but can be omitted for a milder version.""",

    "How do I make Caesar salad",
    """For a classic Caesar salad:
Make an emulsified dressing with garlic, lemon, anchovy (optional), and oil; toss with romaine, croutons, and Parmesan.""",

    "Recipe for Caesar salad",
    """For a classic Caesar salad:
See dressing and salad assembly above — key is a properly emulsified dressing and crisp romaine.""",

    "Can you give me Caesar salad recipe",
    """For a classic Caesar salad:
Combine egg yolk/mayo with garlic, anchovy, lemon, mustard, slowly whisk in oil, toss with romaine, croutons, and Parmesan.""",

    "How to cook Caesar salad",
    """For a classic Caesar salad:
No cooking needed — assemble crisp lettuce, toss with dressing, and add croutons and cheese; grill protein if desired.""",

    "Make Caesar salad",
    """For a classic Caesar salad:
Prepare dressing first, then toss with washed romaine and croutons; finish with grated Parmesan and cracked pepper.""",

    "Show me how to make Caesar salad",
    """For a classic Caesar salad:
Whisk or blender-emulsify the dressing, toss with lettuce, add croutons and Parmesan, optionally top with grilled chicken.""",

    "Best Caesar salad recipe",
    """For a classic Caesar salad:
Use fresh Romaine, properly emulsified dressing, good Parmesan, and homemade croutons for the best texture and flavor.""",


    # VEGETABLE OMELETTE - 8 phrasings
    "How to make vegetable omelette",
    """For a vegetable omelette (1–2 servings):
Ingredients:
- 3 large eggs
- 2 tbsp milk or water
- 1/4 cup chopped bell peppers, 1/4 cup chopped onion, handful spinach or tomatoes
- Salt and pepper to taste
- 1–2 tbsp butter or oil
Steps:
1. Whisk eggs with milk, salt, and pepper until slightly frothy.
2. Sauté vegetables in a non-stick pan with a little oil until softened; push them to the side.
3. Add butter, pour beaten eggs over vegetables, tilt pan to spread evenly.
4. When the edges set and top is slightly moist, fold omelette in half and slide onto a plate. Serve hot.

Tips:
- Cook vegetables first so omelette remains tender and not watery.
- Add cheese before folding for a gooey finish.""",

    "How do I make vegetable omelette",
    """For a vegetable omelette:
Sauté veggies, whisk eggs with a splash of milk, pour eggs into pan, cook until set, fold and serve.""",

    "Recipe for vegetable omelette",
    """For a vegetable omelette:
Use 3 eggs, a splash of milk, sautéed vegetables of choice, and cook in butter until set; add cheese if desired.""",

    "Can you give me vegetable omelette recipe",
    """For a vegetable omelette:
Whisk eggs with milk, cook vegetables first, then pour eggs, fold when cooked, and serve with toast.""",

    "How to cook vegetable omelette",
    """For a vegetable omelette:
Preheat pan, sauté vegetables until softened, add beaten eggs, cook gently, fold and plate.""",

    "Make vegetable omelette",
    """For a vegetable omelette:
Combine eggs and veggies with seasonings, cook quickly in a hot pan, and fold; garnish with herbs.""",

    "Show me how to make vegetable omelette",
    """For a vegetable omelette:
Sauté finely chopped vegetables, whisk eggs, pour over them, let set, fold and serve with bread or salad.""",

    "Best vegetable omelette recipe",
    """For a vegetable omelette:
Use high heat for a quick cook, finely chop vegetables to cook evenly, and add a little dairy (milk or cream) for softness.""",


    # CHICKEN BIRYANI (Simplified) - 8 phrasings
    "How to make chicken biryani",
    """For a simplified chicken biryani (serves 4):
Ingredients:
- 500g chicken pieces
- 2 cups basmati rice, rinsed and soaked 20–30 min
- 2 large onions, thinly sliced and fried until golden
- 2 tomatoes, chopped
- 1/2 cup yogurt
- 2–3 tbsp biryani masala (or ground spices: cumin, coriander, garam masala)
- 1 tsp turmeric, 1–2 tsp chili powder
- 4 cups water or as needed
- Fresh mint and cilantro, lemon juice
- 3–4 tbsp oil/ghee
Steps:
1. Par-cook rice in boiling salted water until 70% done, drain.
2. In a heavy pot, heat oil/ghee, sauté onions until deep golden (save some for garnish), add ginger-garlic paste and tomatoes, cook until soft.
3. Add chicken, yogurt, spices, and cook until chicken is partly done and oil separates.
4. Layer half the par-cooked rice over the chicken, sprinkle mint, cilantro, fried onions and a squeeze of lemon. Add remaining rice and repeat.
5. Cover tightly and cook on very low heat (dum) for 20–25 minutes to finish rice and allow flavors to meld.
6. Gently fluff and serve hot with raita or salad.

Tips:
- Use par-cooked rice (not fully cooked) so final steaming finishes it without becoming mushy.
- Saffron soaked in warm milk and drizzled between layers adds aroma and color.""",

    "How do I make chicken biryani",
    """For a simplified chicken biryani:
Layer partially cooked basmati rice over spiced chicken, add herbs and fried onions, and steam on low until rice finishes cooking and absorbs aroma.""",

    "Recipe for chicken biryani",
    """For a simplified chicken biryani:
Par-boil rice, prepare spiced chicken gravy, layer rice and chicken, cover and cook on low heat (dum) until fully cooked; garnish with fried onions and herbs.""",

    "Can you give me chicken biryani recipe",
    """For a simplified chicken biryani:
Follow par-cooking rice + layered dum method; use biryani masala or whole spices, add yogurt for richness, and garnish with fried onions.""",

    "How to cook chicken biryani",
    """For a simplified chicken biryani:
Cook rice until slightly underdone, prepare chicken masala, layer them together and steam on low heat for the final finish.""",

    "Make chicken biryani",
    """For a simplified chicken biryani:
Par-cook rice, make a flavorful chicken base, layer, and dum-cook until fragrant and tender; serve with raita.""",

    "Show me how to make chicken biryani",
    """For a simplified chicken biryani:
Sear chicken in spices, parboil basmati rice, layer with herbs and fried onions, cover tightly and steam on low to let flavors marry.""",

    "Best chicken biryani recipe",
    """For a simplified chicken biryani:
Use good basmati rice, do not overcook rice before layering, and allow a proper low-heat dum (20–30 minutes) for authentic texture and aroma.""",


    # GUACAMOLE - 8 phrasings
    "How to make guacamole",
    """For a simple guacamole (serves 2–3):
Ingredients:
- 2 ripe avocados
- 1 small tomato, deseeded and finely chopped
- 2 tbsp red onion, finely chopped
- 1 small lime (juice)
- 1 tbsp cilantro, chopped
- Salt and pepper to taste
- 1/4 tsp cumin or pinch chili flakes (optional)
Steps:
1. Halve avocados, remove pit, scoop flesh into a bowl. Mash with a fork until you reach desired texture (chunky or smooth).
2. Add lime juice immediately to prevent browning.
3. Fold in chopped tomato, red onion, cilantro, salt, and pepper. Taste and adjust seasoning.
4. Serve with tortilla chips or as a topping for tacos.

Tips:
- Use lime not lemon for authentic flavor; don’t overmix to keep some texture.
- If not using immediately, press plastic wrap directly onto guacamole surface to reduce browning.""",

    "How do I make guacamole",
    """For simple guacamole:
Mash ripe avocados, add lime juice, chopped onion, tomato, cilantro, salt, and mix; serve immediately.""",

    "Recipe for guacamole",
    """For simple guacamole:
Use 2 ripe avocados, 1 small tomato, lime juice, onion, cilantro, salt, and optional chili; mash and serve.""",

    "Can you give me guacamole recipe",
    """For simple guacamole:
Scoop and mash avocados, add lime juice, red onion, tomato, cilantro, and season to taste; keep chilled until serving.""",

    "How to cook guacamole",
    """For simple guacamole:
No cooking — simply mash and combine fresh ingredients and serve cold or room temperature with chips or as a condiment.""",

    "Make guacamole",
    """For simple guacamole:
Choose ripe avocados (yield slightly to gentle pressure), mash, season with lime, onion, cilantro and salt; optional jalapeño for heat.""",

    "Show me how to make guacamole",
    """For simple guacamole:
Cut avocados, mash, mix in lime, onion, tomato and cilantro; adjust salt and serve promptly to enjoy peak freshness.""",

    "Best guacamole recipe",
    """For simple guacamole:
Use perfectly ripe avocados, bright lime juice, and just enough salt; add fresh cilantro and a small amount of chopped chili if you like heat.""",


    # MANGO SMOOTHIE - 8 phrasings
    "How to make mango smoothie",
    """For a creamy mango smoothie (serves 2):
Ingredients:
- 2 cups ripe mango chunks (fresh or frozen)
- 1 cup milk or dairy-free milk (adjust for thickness)
- 1/2 cup yogurt (optional for creaminess)
- 1–2 tbsp honey or sugar to taste (optional)
- Ice cubes if using fresh mango
Steps:
1. Combine all ingredients in a blender and blend until smooth.
2. Taste and adjust sweetness or thickness (add more milk to thin, more mango or ice to thicken).
3. Pour into glasses and serve immediately.

Tips:
- Frozen mango cubes make the smoothie thick and cold without extra ice.
- Add a pinch of cardamom for an aromatic twist.""",

    "How do I make mango smoothie",
    """For a creamy mango smoothie:
Blend mango, milk, yogurt (optional), and sweetener until smooth; serve chilled.""",

    "Recipe for mango smoothie",
    """For a creamy mango smoothie:
2 cups mango, 1 cup milk, 1/2 cup yogurt, blend until smooth; adjust sweetness to taste.""",

    "Can you give me mango smoothie recipe",
    """For a creamy mango smoothie:
Use ripe mangoes and a creamy base (milk or yogurt), blend and enjoy immediately for best texture and flavor.""",

    "How to cook mango smoothie",
    """For a creamy mango smoothie:
No cooking needed — just blend the fruits and liquids until smooth.""",

    "Make mango smoothie",
    """For a creamy mango smoothie:
Combine mango, milk or yogurt, sweetener, and ice in blender; blend until silky and serve chilled.""",

    "Show me how to make mango smoothie",
    """For a creamy mango smoothie:
Place ingredients in blender, start on low then increase speed, blend until smooth, pour and drink fresh.""",

    "Best mango smoothie recipe",
    """For a creamy mango smoothie:
Use ripe or frozen mango, full-fat yogurt for creaminess, and balance sweetness with a touch of lime or cardamom for brightness.""",


    # VEGETABLE SOUP - 8 phrasings
    "How to make vegetable soup",
    """For a comforting vegetable soup (serves 4):
Ingredients:
- 2 tbsp olive oil
- 1 onion, chopped
- 2 carrots, diced
- 2 celery stalks, diced
- 2 potatoes, peeled and diced
- 1 cup green beans or peas
- 1 can (400g) diced tomatoes or 2 fresh tomatoes
- 6 cups vegetable or chicken stock
- 1 bay leaf, 1 tsp dried thyme
- Salt & pepper, fresh parsley to finish
Steps:
1. In a large pot, heat oil and sauté onion, carrot, and celery for 5–7 minutes until softened.
2. Add potatoes, green beans, tomatoes, herbs, and stock. Bring to a boil, then simmer 20–25 minutes until vegetables are tender.
3. Adjust seasoning, remove bay leaf, and finish with chopped parsley. For a creamier soup, blend part or all and return to pot.
4. Serve hot with crusty bread.

Tips:
- Use seasonal vegetables or leftover roasted veg to add depth.
- For extra protein add cooked beans or shredded chicken.""",

    "How do I make vegetable soup",
    """For a comforting vegetable soup:
Sauté aromatics, add chopped vegetables and stock, simmer until tender, season, and optionally blend for creaminess.""",

    "Recipe for vegetable soup",
    """For a comforting vegetable soup:
See ingredient list above — key: build flavor with sautéed onions and celery, then simmer vegetables until tender.""",

    "Can you give me vegetable soup recipe",
    """For a comforting vegetable soup:
Combine mixed vegetables with stock and herbs, simmer until soft, adjust seasoning, and serve with bread.""",

    "How to cook vegetable soup",
    """For a comforting vegetable soup:
Simmer mixed vegetables in stock with herbs until tender; blend if you prefer a smooth consistency.""",

    "Make vegetable soup",
    """For a comforting vegetable soup:
Sauté base vegetables, add stock and other veg, simmer, season, and serve warm.""",

    "Show me how to make vegetable soup",
    """For a comforting vegetable soup:
Start by sweating onions/celery/carrots, add stock and remaining veg, simmer, season, and finish with fresh herbs.""",

    "Best vegetable soup recipe",
    """For a comforting vegetable soup:
Use homemade stock if possible, sauté base aromatics well, and finish with fresh herbs and a good grind of black pepper for brightness.""",


    # STIR-FRIED NOODLES (Chow Mein style) - 8 phrasings
    "How to make stir-fried noodles",
    """For simple stir-fried noodles (serves 3-4):
Ingredients:
- 300g fresh or dried egg noodles (or chow mein / chow fun)
- 2 tbsp vegetable oil
- 2 cloves garlic, sliced
- 1 cup mixed vegetables (cabbage, carrots, bell pepper)
- 2–3 spring onions, chopped
- 3 tbsp light soy sauce, 1 tbsp dark soy (optional), 1 tsp sesame oil
- Protein optional: tofu, chicken, or shrimp
Steps:
1. Cook noodles according to package (if using dried), drain and toss with a little oil to prevent sticking.
2. Heat wok or large pan on high heat, add oil, sauté garlic briefly, add protein (if using) and cook through; set aside.
3. Add vegetables and stir-fry quickly until just tender-crisp.
4. Add noodles and sauces, toss vigorously to combine and heat through. Return protein and spring onions, drizzle sesame oil and toss once more.
5. Serve immediately.

Tips:
- High heat and quick tossing prevent soggy noodles and give a slight char.
- Prep all ingredients before starting — stir-frying is fast.""",

    "How do I make stir-fried noodles",
    """For simple stir-fried noodles:
Use cooked-and-cooled noodles, high heat, quick stir-fry of vegetables and protein, and finish with soy and sesame oil.""",

    "Recipe for stir-fried noodles",
    """For simple stir-fried noodles:
Cook noodles, stir-fry veggies and protein separately, then combine with soy-based sauce and toss on high heat.""",

    "Can you give me stir-fried noodles recipe",
    """For simple stir-fried noodles:
Noodles + mixed vegetables + soy sauce + sesame oil; quick cooking on high heat for best texture.""",

    "How to cook stir-fried noodles",
    """For simple stir-fried noodles:
Prep ingredients, cook noodles ahead, and stir-fry everything quickly on high heat to keep texture and flavor.""",

    "Make stir-fried noodles",
    """For simple stir-fried noodles:
Follow the steps above; use day-old or well-drained noodles and high heat for the ideal result.""",

    "Show me how to make stir-fried noodles",
    """For simple stir-fried noodles:
Sauté aromatics, cook protein, stir-fry veggies, add drained noodles and sauce, toss to combine, and serve hot.""",

    "Best stir-fried noodles recipe",
    """For simple stir-fried noodles:
Use very high heat, a wide wok if available, and minimal sauce so the noodles crisp slightly and flavors stay balanced.""",
]
