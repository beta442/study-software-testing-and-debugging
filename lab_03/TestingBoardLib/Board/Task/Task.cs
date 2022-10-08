namespace TestingBoardLib.Board.Task
{
    public class Task : ITask
    {
        private readonly string _name;
        private readonly string _description;
        private readonly int _priority;

        public Task(string name, string description, int priority)
        {
            _name = name;
            _description = description;
            _priority = priority;
        }

        public string GetName()
        {
            return _name;
        }

        public string GetDescription()
        {
            return _description;
        }

        public int GetPriority()
        {
            return _priority;
        }
    }
}
