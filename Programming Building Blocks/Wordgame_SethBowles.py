# underline = '\33[4m'
underline = '\u0332'


print ('\nPlease enter the following: \n\n')

adj = input ('Please enter in an adjective: ') or 'blue'
anml = input ('Please name an animal: ') or 'turtle'
verb1 = input ('Please list a verb: ') or 'zoomin'
excl = input ('Please shout something: ') or 'boom'
verb2 = input ('Please list a second verb: ') or 'shuffle'
verb3 = input ('Please list a third verb: ') or 'sleep'
noun1 = input ('Please list a noun: ') or 'shoe'
verb4 = input ('Please list a fourth verb: ') or 'eat'
bop = input ('Please list an Onomatopoeia (Word that sounds like its spelling): ') or 'pit pat'

print ('\nYour story is:\n\n ')
print (f'The other day, I was really in trouble. It all started when I saw a very')
# print (f'{adj} {anml} {verb1} down the hallway. "{excl.capitalize()}!" I yelled. But all')
print ('{:s}{:s}{:s}down the hallway. "{:s}" I yelled. But all'.format(underline.join(adj+' '),underline.join(anml+' '),underline.join(verb1+' '),underline.join(excl.capitalize()+'!')))
print ('I could think to do was to {:s} over and over. Miraculously,'.format(underline.join(verb2+' ')))
print ('that caused it to stop, but not before it tried to {:s}'.format(underline.join(verb3+' ')))
print (f'right in front of my family.')
print ('\"Thank goodness I had my trusty {:s} with me, but I think'.format(underline.join(noun1+' ')))
print ('it is time to go {:s}.\" I say as I {:s} away.\n'.format(underline.join(verb4+' '),underline.join(bop+' ')))
