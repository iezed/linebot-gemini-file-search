"""
File Manager Agent using Google Gemini.
Provides conversational interface for managing files.
"""

import os
from google.adk.agents import Agent
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from .tools import list_files_tool


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or ""
APP_NAME = "file_manager"


class FileManagerAgent:
    """
    Agent for managing files in a conversational way.
    Uses Gemini to generate natural, conversational responses.
    """

    def __init__(self, store_name: str, store_name_cache: dict):
        """
        Initialize the File Manager Agent.

        Args:
            store_name: The display name of the file search store
            store_name_cache: Cache mapping display_name to actual store name
        """
        self.store_name = store_name
        self.store_name_cache = store_name_cache

        # Create a wrapper function that captures the context
        async def list_files():
            """列出使用者已上傳的所有文件檔案，包含檔案名稱和上傳時間。"""
            return await list_files_tool(self.store_name, self.store_name_cache)

        # Store the wrapper function
        self._list_files = list_files

        # Initialize the ADK Agent with the callable function
        self.agent = Agent(
            name="file_manager",
            model="gemini-2.5-flash",
            description="檔案管理助手，幫助使用者查看和管理已上傳的文件。",
            instruction="""你是一個友善的檔案管理助手。
當使用者想要查看檔案時，使用 list_files 工具獲取檔案清單。
請用自然、口語化的方式向使用者介紹這些檔案，不要使用條列式，用對話的方式說明。
讓使用者感覺像在跟朋友聊天一樣。""",
            tools=[self._list_files],  # Pass the callable function
        )

        # Initialize session service and runner
        self.session_service = InMemorySessionService()
        self.runner = Runner(
            app_name=APP_NAME,
            agent=self.agent,
            session_service=self.session_service
        )

    async def handle_list_files(self) -> str:
        """
        Handle list files request in a conversational way.

        Returns:
            Conversational response about the files
        """
        try:
            # Create a session for this interaction
            user_id = f"user_{self.store_name}"
            session = await self.session_service.create_session(
                app_name=APP_NAME,
                user_id=user_id,
                session_id=f"list_files_{self.store_name}"
            )

            # Create the user message
            user_prompt = "請列出所有已上傳的檔案"
            content = types.Content(
                role="user",
                parts=[types.Part(text=user_prompt)]
            )

            # Run the agent and collect responses
            response_texts = []
            async for event in self.runner.run_async(
                user_id=user_id,
                session_id=session.id,
                new_message=content
            ):
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            response_texts.append(part.text)

            # Join all response texts
            if response_texts:
                return '\n'.join(response_texts)
            else:
                return "目前沒有找到任何檔案唷！"

        except Exception as e:
            print(f"Error in FileManagerAgent: {e}")
            import traceback
            traceback.print_exc()
            return f"查詢檔案時發生了一點問題：{str(e)}"
