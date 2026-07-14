# main.py

import time
import signal
import sys
from datetime import datetime

from agent.brain import Brain
from agent.memory import Memory
from agent.planner import Planner


class AgentRunner:

    def __init__(self):
        self.running = True

        self.memory = Memory()
        self.brain = Brain()
        self.planner = Planner()

        print("🤖 Agent started 24/7 mode")

    def shutdown(self, signal, frame):
        print("\n🛑 Shutting down agent...")
        self.running = False
        sys.exit(0)


    def heartbeat(self):
        """
        Ciclo de vida del agente.
        """

        print(
            f"\n💓 Heartbeat {datetime.now()}"
        )


        # 1. Leer memoria
        context = self.memory.load()


        # 2. Pensar qué hacer
        task = self.planner.create_task(context)


        if task:

            print(f"📌 Task detected: {task}")


            # 3. Pasar al cerebro
            result = self.brain.think(task)


            print("✅ Result:")
            print(result)


            # 4. Guardar aprendizaje
            self.memory.save(
                task,
                result
            )


        else:
            print("😴 No tasks. Waiting...")


    def run(self):

        while self.running:

            try:

                self.heartbeat()


                # espera entre ciclos
                # ejemplo: cada 10 minutos
                time.sleep(
                    600
                )


            except Exception as error:

                print(
                    "❌ Agent error:",
                    error
                )


                # evita morir
                time.sleep(60)



if __name__ == "__main__":

    agent = AgentRunner()


    # Ctrl+C limpio
    signal.signal(
        signal.SIGINT,
        agent.shutdown
    )


    signal.signal(
        signal.SIGTERM,
        agent.shutdown
    )


    agent.run()