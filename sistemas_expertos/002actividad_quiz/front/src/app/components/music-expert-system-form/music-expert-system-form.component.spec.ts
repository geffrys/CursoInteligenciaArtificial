import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MusicExpertSystemFormComponent } from './music-expert-system-form.component';

describe('MusicExpertSystemFormComponent', () => {
  let component: MusicExpertSystemFormComponent;
  let fixture: ComponentFixture<MusicExpertSystemFormComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MusicExpertSystemFormComponent]
    });
    fixture = TestBed.createComponent(MusicExpertSystemFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
