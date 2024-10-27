from app.nodes import _get_open_ai, report_agent
from langchain_openai import ChatOpenAI


def test_node_setup():
    pass


def test_get_open_ai(setup_environment):
    _, _, tools, _ = setup_environment

    llm = _get_open_ai().bound
    assert isinstance(llm, ChatOpenAI)
    assert llm.temperature == 0


def test_report_agent(mocker, setup_environment):
    _, _, _, current_tools = setup_environment

    state = {
        "selected_tools": ["test_tool_id"],
        "messages": [{"content": "tool information"}],
    }

    mock_llm = mocker.Mock()
    mock_bound_llm = mocker.Mock()
    mock_bound_llm.invoke.return_value = "Test response"

    mock_llm.bind_tools.return_value = mock_bound_llm

    # Mock the ChatOpenAI instance returned by _get_open_ai
    mocker.patch("app.nodes._get_open_ai", return_value=mock_llm)

    result = report_agent(state)

    assert result == {"messages": ["Test response"]}
