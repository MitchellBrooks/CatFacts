import subprocess
import threading
import random
import sched
import time

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def do_something(sc): 
    print ("About to copy...")
    s.enter(0.5, 1, do_something, (sc,))

    copy2clip(
        random.choice ([
                'Smuggling a cat out of ancient Egypt was punishable by death. Phoenician traders eventually succeeded in smuggling felines, which they sold to rich people in Athens and other important cities.',
                'The earliest ancestor of the modern cat lived about 30 million years ago. Scientists called it the Proailurus, which means “first cat” in Greek. The group of animals that pet cats belong to emerged around 12 million years ago.',
                'The biggest wildcat today is the Siberian Tiger. It can be more than 12 feet (3.6 m) long (about the size of a small car) and weigh up to 700 pounds (317 kg).',
                'The smallest wildcat today is the Black-footed cat. The females are less than 20 inches (50 cm) long and can weigh as little as 2.5 lbs (1.2 kg).',
                'Many Egyptians worshipped the goddess Bast, who had a woman’s body and a cat’s head.',
                'Mohammed loved cats and reportedly his favorite cat, Muezza, was a tabby. Legend says that tabby cats have an “M” for Mohammed on top of their heads because Mohammad would often rest his hand on the cat’s head.',
                'While many parts of Europe and North America consider the black cat a sign of bad luck, in Britain and Australia, black cats are considered lucky.',
                'The most popular pedigreed cat is the Persian cat, followed by the Main Coon cat and the Siamese cat.',
                'The smallest pedigreed cat is a Singapura, which can weigh just 4 lbs (1.8 kg), or about five large cans of cat food. The largest pedigreed cats are Maine Coon cats, which can weigh 25 lbs (11.3 kg), or nearly twice as much as an average cat weighs.',
                'n Holland’s embassy in Moscow, Russia, the staff noticed that the two Siamese cats kept meowing and clawing at the walls of the building. Their owners finally investigated, thinking they would find mice. Instead, they discovered microphones hidden by Russian spies. The cats heard the microphones when they turned on.',
                'The little tufts of hair in a cat’s ear that help keep out dirt direct sounds into the ear, and insulate the ears are called “ear furnishings.”',
                'The ability of a cat to find its way home is called “psi-traveling.” Experts think cats either use the angle of the sunlight to find their way or that cats have magnetized cells in their brains that act as compasses.',
                'Isaac Newton invented the cat flap. Newton was experimenting in a pitch-black room. Spithead, one of his cats, kept opening the door and wrecking his experiment. The cat flap kept both Newton and Spithead happy.',
                'The world’s rarest coffee, Kopi Luwak, comes from Indonesia where a wildcat known as the luwak lives. The cat eats coffee berries and the coffee beans inside pass through the stomach. The beans are harvested from the cat\'s dung heaps and then cleaned and roasted. Kopi Luwak sells for about $500 for a 450 g (1 lb) bag.',
                'A cat’s jaw can’t move sideways, so a cat can’t chew large chunks of food.',
                'A cat almost never meows at another cat, mostly just humans. Cats typically will spit, purr, and hiss at other cats.',
                'A cat’s back is extremely flexible because it has up to 53 loosely fitting vertebrae. Humans only have 34.',
                'Approximately 1/3 of cat owners think their pets are able to read their minds.',
                'All cats have claws, and all except the cheetah sheath them when at rest.',
                'Two members of the cat family are distinct from all others: the clouded leopard and the cheetah. The clouded leopard does not roar like other big cats, nor does it groom or rest like small cats. The cheetah is unique because it is a running cat; all others are leaping cats. They are leaping cats because they slowly stalk their prey and then leap on it.',
                'A cat lover is called an Ailurophilia (Greek: cat+lover).',
                'In Japan, cats are thought to have the power to turn into super spirits when they die. This may be because according to the Buddhist religion, the body of the cat is the temporary resting place of very spiritual people.',
                'Most cats had short hair until about 100 years ago, when it became fashionable to own cats and experiment with breeding.',
                'Cats have 32 muscles that control the outer ear (humans have only 6). A cat can independently rotate its ears 180 degrees.',
                'One reason that kittens sleep so much is because a growth hormone is released only during sleep.',
                'Cats have about 130,000 hairs per square inch (20,155 hairs per square centimeter).',
                'The heaviest cat on record is Himmy, a Tabby from Queensland, Australia. He weighed nearly 47 pounds (21 kg). He died at the age of 10.',
                'The oldest cat on record was Crème Puff from Austin, Texas, who lived from 1967 to August 6, 2005, three days after her 38th birthday. A cat typically can live up to 20 years, which is equivalent to about 96 human years.',
                'The lightest cat on record is a blue point Himalayan called Tinker Toy, who weighed 1 pound, 6 ounces (616 g). Tinker Toy was 2.75 inches (7 cm) tall and 7.5 inches (19 cm) long.',
                'The tiniest cat on record is Mr. Pebbles, a 2-year-old cat that weighed 3 lbs (1.3 k) and was 6.1 inches (15.5 cm) high.',
                'A commemorative tower was built in Scotland for a cat named Towser, who caught nearly 30,000 mice in her lifetime.',
                'In the 1750s, Europeans introduced cats into the Americas to control pests.',
                'The first cat show was organized in 1871 in London. Cat shows later became a worldwide craze.',
                'The first cartoon cat was Felix the Cat in 1919. In 1940, Tom and Jerry starred in the first theatrical cartoon “Puss Gets the Boot.” In 1981 Andrew Lloyd Weber created the musical Cats, based on T.S. Eliot’s Old Possum’s Book of Practical Cats.',
                'The normal body temperature of a cat is between 100.5 ° and 102.5 °F. A cat is sick if its temperature goes below 100 ° or above 103 °F.',
                'A cat has 230 bones in its body. A human has 206. A cat has no collarbone, so it can fit through any opening the size of its head.',
                'A cat’s nose pad is ridged with a unique pattern, just like the fingerprint of a human.',
                'If they have ample water, cats can tolerate temperatures up to 133 °F.',
                'Foods that should not be given to cats include onions, garlic, green tomatoes, raw potatoes, chocolate, grapes, and raisins. Though milk is not toxic, it can cause an upset stomach and gas. Tylenol and aspirin are extremely toxic to cats, as are many common houseplants. Feeding cats dog food or canned tuna that\'s for human consumption can cause malnutrition.',
                'A 2007 Gallup poll revealed that both men and women were equally likely to own a cat.',
                'A cat’s heart beats nearly twice as fast as a human heart, at 110 to 140 beats a minute.',
                'Cats don’t have sweat glands over their bodies like humans do. Instead, they sweat only through their paws.',
                'In just seven years, a single pair of cats and their offspring could produce a staggering total of 420,000 kittens.',
                'Relative to its body size, the clouded leopard has the biggest canines of all animals\' canines. Its dagger-like teeth can be as long as 1.8 inches (4.5 cm).',
                'Cats spend nearly 1/3 of their waking hours cleaning themselves.',
                'Grown cats have 30 teeth. Kittens have about 26 temporary teeth, which they lose when they are about 6 months old.',
                'A cat called Dusty has the known record for the most kittens. She had more than 420 kittens in her lifetime.',
                'The largest cat breed is the Ragdoll. Male Ragdolls weigh between 12 and 20 lbs (5.4-9.0 k). Females weigh between 10 and 15 lbs (4.5-6.8 k).',
                'Cats are extremely sensitive to vibrations. Cats are said to detect earthquake tremors 10 or 15 minutes before humans can.',
                'In contrast to dogs, cats have not undergone major changes during their domestication process.',
                'A female cat is called a queen or a molly.',
                'In the 1930s, two Russian biologists discovered that color change in Siamese kittens depend on their body temperature. Siamese cats carry albino genes that work only when the body temperature is above 98° F. If these kittens are left in a very warm room, their points won’t darken and they will stay a creamy white.',
                'There are up to 60 million feral cats in the United States alone.',
                'The oldest cat to give birth was Kitty who, at the age of 30, gave birth to two kittens. During her life, she gave birth to 218 kittens.',
                'The most traveled cat is Hamlet, who escaped from his carrier while on a flight. He hid for seven weeks behind a pane. By the time he was discovered, he had traveled nearly 373,000 miles (600,000 km).',
                'The most expensive cat was an Asian Leopard cat (ALC)-Domestic Shorthair (DSH) hybrid named Zeus. Zeus, who is 90% ALC and 10% DSH, has an asking price of £100,000 ($154,000).',
                'The cat who holds the record for the longest non-fatal fall is Andy. He fell from the 16th floor of an apartment building (about 200 ft/.06 km) and survived.',
                'The richest cat is Blackie who was left £15 million by his owner, Ben Rea.',
                'The claws on the cat’s back paws aren’t as sharp as the claws on the front paws because the claws in the back don’t retract and, consequently, become worn.'
            ])
        )
    print("Done!")



s = sched.scheduler(time.time, time.sleep)
s.enter(0.5, 1, do_something, (s,))
s.run()
