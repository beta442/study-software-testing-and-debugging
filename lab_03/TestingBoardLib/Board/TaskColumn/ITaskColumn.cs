using TestingBoardLib.Board.Task;

namespace TestingBoardLib.Board.TaskColumn
{
    public interface ITaskColumn
    {
        void AddPrioritedTaskList(int taskPriority);
        void AddTask(ITask task);
        string GetName();
        IReadOnlyDictionary<int, List<ITask>> GetPrioritedTaskMap();
        ITask GetTaskBy(int taskPriority, int taskNumber);
        int GetPrioritedTaskCount(int taskPriority);
        int GetPrioritedTaskIndex(int taskPriority, string taskName);
        int GetTaskCount();
        bool HasColumnPrioritedTasks(int taskPriority);
        void RemovePrioritedTaskList(int taskListPriority);
        void RemoveTask(int taskPriority, int taskNumber);
        void Rename(string name);
    }
}
