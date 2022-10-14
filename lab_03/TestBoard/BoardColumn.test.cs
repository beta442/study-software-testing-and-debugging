using Moq;
using TestingBoardLib.Board.Task;
using TestingBoardLib.Board.TaskColumn;

namespace TestBoard
{
    public class TestBoardTaskColumn
    {
        private readonly TaskColumn _tC;

        public TestBoardTaskColumn()
        {
            _tC = new();
        }

        [Fact]
        public void Creating_taskColumn_with_empty_name()
        {
            const string expectedName = "Column";

            string actualName = _tC.GetName();

            Assert.Equal(expectedName, actualName);
        }

        [Fact]
        public void Creating_taskColumn_with_empty_string()
        {
            const string expectedName = "Column";
            TaskColumn tC = new("");

            string actualName = tC.GetName();

            Assert.Equal(expectedName, actualName);
        }

        [Fact]
        public void Creating_taskColumn_with_provided_name()
        {
            const string expectedName = "Name";
            TaskColumn tC = new(expectedName);

            string actualName = tC.GetName();

            Assert.Equal(expectedName, actualName);
        }

        [Fact]
        public void New_taskColumn_doesnt_contain_any_tasks()
        {
            const int expectedTaskCount = 0;

            int actualTaskCount = _tC.GetTaskCount();

            Assert.Equal(expectedTaskCount, actualTaskCount);
            Assert.Empty(_tC.GetPrioritedTaskMap());
        }

        [Fact]
        public void Renaming_taskColumn()
        {
            const string newName = "NewName";

            _tC.Rename(newName);

            Assert.Equal(newName, _tC.GetName());
        }

        [Fact]
        public void Renaming_taskColumn_with_empty_name()
        {
            const string newName = "";
            const string expectedName = "Column";

            _tC.Rename(newName);

            Assert.Equal(expectedName, _tC.GetName());
        }

        [Fact]
        public void Removing_task_with_negative_number_throws()
        {
            Assert.Throws<Exception>(delegate { _tC.RemoveTask(0, -10); });
        }

        [Fact]
        public void Remove_a_task_with_a_non_existent_priority_in_the_column_throws()
        {
            Assert.Throws<Exception>(delegate { _tC.RemoveTask(10, 0); });
        }

        [Fact]
        public void Removing_task_with_number_higher_than_prioritedTaskList_has_throws()
        {
            const int taskPriority = 10;
            _tC.AddPrioritedTaskList(taskPriority);

            Assert.Throws<Exception>(delegate { _tC.RemoveTask(taskPriority, 10); });
        }

        [Fact]
        public void Getting_task_with_negative_number_throws()
        {
            Assert.Throws<Exception>(delegate { _tC.GetTaskBy(0, -10); });
        }

        [Fact]
        public void Getting_a_task_with_a_non_existent_priority_in_the_column_throws()
        {
            Assert.Throws<Exception>(delegate { _tC.RemoveTask(10, 0); });
        }

        [Fact]
        public void Getting_task_with_number_higher_than_prioritedTaskList_has_throws()
        {
            const int taskPriority = 10;
            _tC.AddPrioritedTaskList(taskPriority);

            Assert.Throws<Exception>(delegate { _tC.RemoveTask(taskPriority, 10); });
        }

        [Fact]
        public void Adding_priorited_taskList()
        {
            _tC.AddPrioritedTaskList(0);

            Assert.True(_tC.GetPrioritedTaskMap().ContainsKey(0));
        }

        [Fact]
        public void Adding_same_priorited_taskList_does_nothing()
        {
            _tC.AddPrioritedTaskList(0);

            _tC.AddPrioritedTaskList(0);

            Assert.Single(_tC.GetPrioritedTaskMap().Keys);
        }

        [Fact]
        public void Removing_not_existing_priorited_taskList_does_nothing()
        {
            _tC.AddPrioritedTaskList(0);

            _tC.RemovePrioritedTaskList(1);

            Assert.Single(_tC.GetPrioritedTaskMap().Keys);
        }

        [Fact]
        public void Removing_priorited_taskList()
        {
            _tC.AddPrioritedTaskList(0);

            _tC.RemovePrioritedTaskList(0);

            Assert.Empty(_tC.GetPrioritedTaskMap());
        }

        [Fact]
        public void Getting_prioritedTaskCount_when_column_hasnt_prioritedTaskList()
        {
            const int expectedResult = -1;
            const int taskPriority = 10;

            Assert.Equal(expectedResult, _tC.GetPrioritedTaskCount(taskPriority));
        }

        [Fact]
        public void Getting_prioritedTask_index_with_bad_arguments()
        {
            const int expectedResult = -1;
            const int taskPriority = 10;
            _tC.AddPrioritedTaskList(taskPriority);

            Assert.Equal(expectedResult, _tC.GetPrioritedTaskIndex(taskPriority, ""));
            Assert.Equal(expectedResult, _tC.GetPrioritedTaskIndex(taskPriority + 1, "SomeName"));
        }

        [Fact]
        public void Getting_taskCount_when_column_contains_empty_prioritedTaskList()
        {
            const int expectedResult = 0;

            for (int i = 0; i < 10; i++)
            {
                _tC.AddPrioritedTaskList(i);
            }

            Assert.Equal(expectedResult, _tC.GetTaskCount());
        }

        [Fact]
        public void Adding_task_also_adds_prioritedTaskList()
        {
            const int taskPriority = 10;
            const string taskName = "Name";
            const string taskDescription = "Description";
            var task = CreateMoqTask(taskName, taskDescription, taskPriority);

            _tC.AddTask(task.Object);

            Assert.True(_tC.HasColumnPrioritedTasks(taskPriority));
        }

        [Fact]
        public void Count_task()
        {
            const int expectedResult = 10;
            const string taskName = "Name";
            const string taskDescription = "Description";

            for (int i = 0; i < expectedResult; i++)
            {
                _tC.AddTask(CreateMoqTask(taskName, taskDescription, i).Object);
            }

            Assert.Equal(expectedResult, _tC.GetTaskCount());
        }

        [Fact]
        public void Getting_task()
        {
            const int taskNumber = 0;
            const int taskPriority = 10;
            const string taskName = "Name";
            const string taskDescription = "Description";
            var task = CreateMoqTask(taskName, taskDescription, taskPriority);
            _tC.AddTask(task.Object);

            var gotTask = _tC.GetTaskBy(taskPriority, taskNumber);

            Assert.Equal(taskName, gotTask.GetName());
            Assert.Equal(taskPriority, gotTask.GetPriority());
            Assert.Equal(taskDescription, gotTask.GetDescription());
        }

        [Fact]
        public void Getting_priorited_task_index()
        {
            const int expectedResult = 0;
            const int taskPriority = 10;
            const string taskName = "Name";
            const string taskDescription = "Description";
            var task = CreateMoqTask(taskName, taskDescription, taskPriority);
            _tC.AddTask(task.Object);

            Assert.Equal(expectedResult, _tC.GetPrioritedTaskIndex(taskPriority, taskName));
            task.Verify(
                t => t.GetName(),
                Times.Once
            );
        }

        [Fact]
        public void Removing_task_from_column_that_contains_only_one_task()
        {
            const int taskNumber = 0;
            const int taskPriority = 10;
            const string taskName = "Name";
            const string taskDescription = "Description";
            var task = CreateMoqTask(taskName, taskDescription, taskPriority);
            _tC.AddTask(task.Object);

            _tC.RemoveTask(taskPriority, taskNumber);

            Assert.Equal(-1, _tC.GetPrioritedTaskCount(taskPriority));
            Assert.Equal(0, _tC.GetTaskCount());
            Assert.Empty(_tC.GetPrioritedTaskMap());
        }

        [Fact]
        public void Removing_task_from_column_that_contains_many_tasks()
        {
            const int taskNumber = 0;
            const int taskPriority = 10;
            const string taskName = "Name";
            const string taskDescription = "Description";
            var task1 = CreateMoqTask(taskName, taskDescription, taskPriority);
            var task2 = CreateMoqTask(taskName, taskDescription, taskPriority);
            _tC.AddTask(task1.Object);
            _tC.AddTask(task2.Object);

            _tC.RemoveTask(taskPriority, taskNumber);

            Assert.Equal(1, _tC.GetPrioritedTaskCount(taskPriority));
            Assert.Equal(1, _tC.GetTaskCount());
            Assert.NotEmpty(_tC.GetPrioritedTaskMap());
            Assert.Equal(task2.Object, _tC.GetPrioritedTaskMap()[taskPriority][taskNumber]);
        }

        private Mock<ITask> CreateMoqTask(string taskName, string taskDescription, int taskPriority)
        {
            var task = new Mock<ITask>();
            task.Setup(t => t.GetPriority()).Returns(taskPriority);
            task.Setup(t => t.GetName()).Returns(taskName);
            task.Setup(t => t.GetDescription()).Returns(taskDescription);

            return task;
        }
    }
}