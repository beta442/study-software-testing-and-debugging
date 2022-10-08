namespace TestingBoardLib.Board.Task
{
    public interface ITask
    {
        public string GetDescription();
        public string GetName();
        public int GetPriority();
    }
}
