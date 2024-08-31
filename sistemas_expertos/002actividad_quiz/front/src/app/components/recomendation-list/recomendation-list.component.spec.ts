import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecomendationListComponent } from './recomendation-list.component';

describe('RecomendationListComponent', () => {
  let component: RecomendationListComponent;
  let fixture: ComponentFixture<RecomendationListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RecomendationListComponent]
    });
    fixture = TestBed.createComponent(RecomendationListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
