# A simple example of well-written and poorly written implementations of the same functionality

def vaccOne():
    return

class Vaccination():
    def __call__(self, simulation_time):
        number_of_vaccinations = 0

        while (number_of_vaccinations < self.daily_dose_capacity
                and not self._population.vaccine_queue.empty()):
            person = self._population.vaccine_queue.get()
            person.vaccinate(simulation_time)
            number_of_vaccinations += 1


def vacc_all(q, t, D):
    # Set a counter for the number of people vaccinated
    N = 0
    # Vaccinate until you run out of people to vaccinate,
    # or until you run out of vaccine doses
    while N<D & int(len(q)>0)==1:
        p = q[len(q)-1] # Get the last person in the queue
        q = q[0:len(q)-1]  # Remove the last person from the queue
        vaccOne(p,t)  # Vaccinate one person and record the time
        N = N +1  # Increment the counter