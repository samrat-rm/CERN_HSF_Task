from pyHepMC3 import HepMC3 as hm
import matplotlib.pyplot as plt

filename = 'data/top.hepmc'
reader = hm.ReaderAscii(filename)
event = hm.GenEvent()

pt_values = []
event_count = 0

while not reader.failed():
    reader.read_event(event)
    if reader.failed():
        break

    event_count += 1
    num_particles = len(list(event.particles()))

    # Compute transverse momentum
    for particle in event.particles():

        if particle.status() == 1:
            px, py = particle.momentum().px(), particle.momentum().py()            
            pt = (px**2 + py**2) ** 0.5 
            pt_values.append(pt)
    
print(f"Event {event_count}: {num_particles} particles")

reader.close()

plt.figure(figsize=(8, 6))
plt.hist(pt_values, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.xlabel("Transverse Momentum (GeV)")
plt.ylabel("Frequency")
plt.title("Histogram of Transverse Momentum for Final State Particles")
plt.grid(True)
plt.show()