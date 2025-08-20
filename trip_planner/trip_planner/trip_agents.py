from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

class TripAgents:

    def city_selection_agent(self):
        return Agent(
            role="City Selector",
            goal="Select the best city for the traveler based on their interests and constraints",
            backstory=("An experienced travel advisor with knowledge of global cities and travel trends. "
                       "Always prefer reliable and official sources (e.g. .nic.in, .gov.in, .org.in) when suggesting cities."),
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    def local_expert(self):
        return Agent(
            role="Local Expert",
            goal="Provide detailed local insights and recommendations for attractions, food, and experiences.",
            backstory=("A local guide with deep knowledge about the culture, attractions, and experiences. "
                       "When scraping websites, avoid unofficial or non-existent domains like .com unless verified. "
                       "Prefer government or tourism board websites (e.g. mysore.nic.in, karnatakatourism.org)."),
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )

    def travel_concierge(self):
        return Agent(
            role="Travel Concierge",
            goal="Build a structured travel plan including transportation, lodging, and activities.",
            backstory=("A professional concierge specialized in planning smooth and enjoyable trips. "
                       "Use only trusted travel sources (official airline, hotel, and tourism websites)."),
            tools=[SerperDevTool()],
            verbose=True
        )
