from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import openai

openai.api_key = '<OPENAI_KEY_HERE>'

def create_agents():
    config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
    assistant = AssistantAgent(name="Assistant", llm_config={"config_list": config_list})
    user_proxy = UserProxyAgent(name="user_proxy",code_execution_config={"work_dir":"coding"})
    return assistant, user_proxy

def main():
    print('Welcome to AutoGen PlayGround!')
    assistant, user_proxy = create_agents()
    # the assistant receives a message from the user, which contains the task description
    user_proxy.initiate_chat(
        assistant,
        message="""Build a mario game""",
    )
    

if __name__ == '__main__':   
    main()
    


