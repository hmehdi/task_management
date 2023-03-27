import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { of } from 'rxjs';

import { TaskSearchComponent } from '../task-search/task-search.component';
import { TaskService } from '../task.service';
import { TASKS } from '../mock-tasks';

import { DashboardComponent } from './dashboard.component';

describe('DashboardComponent', () => {
  let component: DashboardComponent;
  let fixture: ComponentFixture<DashboardComponent>;
  let taskService;
  let getTasksSpy: jasmine.Spy;

  beforeEach(waitForAsync(() => {
    taskService = jasmine.createSpyObj('TaskService', ['getTasks']);
    getTasksSpy = taskService.getTasks.and.returnValue(of(TASKS));
    TestBed
        .configureTestingModule({
          declarations: [DashboardComponent, TaskSearchComponent],
          imports: [RouterTestingModule.withRoutes([])],
          providers: [{provide: TaskService, useValue: taskService}]
        })
        .compileComponents();

    fixture = TestBed.createComponent(DashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should be created', () => {
    expect(component).toBeTruthy();
  });

  it('should display "Top Tasks" as headline', () => {
    expect(fixture.nativeElement.querySelector('h2').textContent).toEqual('Top Tasks');
  });

  it('should call taskService', waitForAsync(() => {
       expect(getTasksSpy.calls.any()).toBe(true);
     }));

  it('should display 4 links', waitForAsync(() => {
       expect(fixture.nativeElement.querySelectorAll('a').length).toEqual(4);
     }));
});
